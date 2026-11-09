<!-- src/views/admin/AdminArticles.vue -->
<script setup lang="ts">
import { nextTick, onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import http from '../../api/http'
import { richTextToPlainText, sanitizeRichText } from '../../utils/richText'

interface Article {
  id: number
  title: string
  content: string
  cover_url: string | null
  summary: string | null
  is_published: boolean
  created_at: string
  updated_at: string
}

const router = useRouter()
const articles = ref<Article[]>([])
const loading = ref(false)
const error = ref('')

const showEditor = ref(false)
const editingId = ref<number | null>(null)
const form = ref({ title: '', content: '', summary: '', is_published: true })
const editorRef = ref<HTMLElement | null>(null)
const saving = ref(false)
const formError = ref('')

function formatDate(iso: string) {
  return new Date(iso).toLocaleString('zh-CN')
}

async function fetchArticles() {
  loading.value = true
  error.value = ''
  try {
    const { data } = await http.get('/articles')
    articles.value = data
  } catch (e: any) {
    error.value = e?.response?.data?.detail ?? '加载失败'
  } finally {
    loading.value = false
  }
}

function openRichTextEditor() {
  showEditor.value = true
  void nextTick(() => {
    if (editorRef.value) editorRef.value.innerHTML = sanitizeRichText(form.value.content)
  })
}

function syncEditor() {
  form.value.content = sanitizeRichText(editorRef.value?.innerHTML || '')
}

function formatText(command: string, value?: string) {
  editorRef.value?.focus()
  document.execCommand(command, false, value)
  syncEditor()
}

function pastePlainText(event: ClipboardEvent) {
  event.preventDefault()
  document.execCommand('insertText', false, event.clipboardData?.getData('text/plain') || '')
  syncEditor()
}
function openCreate() {
  editingId.value = null
  form.value = { title: '', content: '', summary: '', is_published: true }
  formError.value = ''
  openRichTextEditor()
}

function openEdit(item: Article) {
  editingId.value = item.id
  form.value = {
    title: item.title,
    content: item.content,
    summary: item.summary ?? '',
    is_published: item.is_published,
  }
  formError.value = ''
  openRichTextEditor()
}

function closeEditor() {
  showEditor.value = false
}

async function save() {
  syncEditor()
  if (!form.value.title.trim() || !richTextToPlainText(form.value.content)) {
    formError.value = '标题和正文不能为空'
    return
  }
  saving.value = true
  formError.value = ''
  try {
    if (editingId.value === null) {
      await http.post('/articles', form.value)
    } else {
      await http.put(`/articles/${editingId.value}`, form.value)
    }
    showEditor.value = false
    await fetchArticles()
  } catch (e: any) {
    formError.value = e?.response?.data?.detail ?? '保存失败'
  } finally {
    saving.value = false
  }
}

async function remove(item: Article) {
  if (!window.confirm(`确定删除文章「${item.title}」吗？此操作不可撤销。`)) return
  try {
    await http.delete(`/articles/${item.id}`)
    await fetchArticles()
  } catch (e: any) {
    error.value = e?.response?.data?.detail ?? '删除失败'
  }
}

function logout() {
  localStorage.removeItem('admin_token')
  router.push('/admin')
}

onMounted(fetchArticles)
</script>

<template>
  <div class="min-h-screen bg-slate-50">
    <header class="sticky top-0 z-10 border-b border-slate-200 bg-white">
      <div class="mx-auto flex max-w-5xl items-center justify-between px-5 py-4">
        <div>
          <span class="text-xs font-bold uppercase tracking-[0.3em] text-brand-red">YIHONG ADMIN</span>
          <h1 class="text-lg font-black text-brand-navy">文章管理</h1>
        </div>
        <div class="flex items-center gap-3">
          <a href="/" class="text-sm text-slate-500 hover:text-brand-red">返回官网</a>
          <button @click="logout" class="rounded-lg border border-slate-300 px-4 py-2 text-sm font-bold text-slate-600 hover:bg-slate-100">退出登录</button>
        </div>
      </div>
    </header>

    <main class="mx-auto max-w-5xl px-5 py-8">
      <div class="mb-6 flex items-center justify-between">
        <button @click="openCreate" class="btn-primary">+ 新建文章</button>
      </div>

      <p v-if="error" class="mb-4 rounded-lg bg-red-50 px-4 py-3 text-sm text-brand-red">{{ error }}</p>

      <div v-if="loading" class="py-16 text-center text-slate-400">加载中…</div>

      <div v-else-if="articles.length === 0" class="rounded-xl border border-dashed border-slate-300 py-16 text-center text-slate-400">
        暂无文章，点击「新建文章」开始发布
      </div>

      <ul v-else class="space-y-3">
        <li
          v-for="item in articles"
          :key="item.id"
          class="flex items-center justify-between gap-4 rounded-xl border border-slate-200 bg-white px-5 py-4"
        >
          <div class="min-w-0">
            <div class="flex items-center gap-2">
              <h2 class="truncate font-bold text-brand-navy">{{ item.title }}</h2>
              <span
                class="shrink-0 rounded-full px-2 py-0.5 text-xs font-bold"
                :class="item.is_published ? 'bg-green-100 text-green-700' : 'bg-slate-200 text-slate-500'"
              >
                {{ item.is_published ? '已发布' : '草稿' }}
              </span>
            </div>
            <p class="mt-1 truncate text-sm text-slate-500">{{ item.summary || richTextToPlainText(item.content) }}</p>
            <p class="mt-1 text-xs text-slate-400">更新于 {{ formatDate(item.updated_at) }}</p>
          </div>
          <div class="flex shrink-0 gap-2">
            <button @click="openEdit(item)" class="rounded-lg border border-slate-300 px-3 py-1.5 text-sm font-bold text-slate-600 hover:bg-slate-100">编辑</button>
            <button @click="remove(item)" class="rounded-lg border border-red-200 px-3 py-1.5 text-sm font-bold text-brand-red hover:bg-red-50">删除</button>
          </div>
        </li>
      </ul>
    </main>

    <!-- 编辑器对话框 -->
    <div v-if="showEditor" class="fixed inset-0 z-20 flex items-center justify-center bg-black/40 px-5" @click.self="closeEditor">
      <div class="max-h-[90vh] w-full max-w-2xl overflow-y-auto rounded-2xl bg-white p-6">
        <h2 class="mb-5 text-xl font-black text-brand-navy">{{ editingId === null ? '新建文章' : '编辑文章' }}</h2>
        <form class="space-y-4" @submit.prevent="save">
          <div>
            <label class="mb-1 block text-sm font-bold text-slate-700">标题</label>
            <input v-model="form.title" type="text" class="w-full rounded-lg border border-slate-300 px-4 py-2.5 text-sm outline-none focus:border-brand-red" placeholder="文章标题" />
          </div>
          <div>
            <label class="mb-1 block text-sm font-bold text-slate-700">摘要（选填）</label>
            <input v-model="form.summary" type="text" class="w-full rounded-lg border border-slate-300 px-4 py-2.5 text-sm outline-none focus:border-brand-red" placeholder="一句话摘要" />
          </div>
          <div>
            <label class="mb-1 block text-sm font-bold text-slate-700">正文</label>
            <div class="overflow-hidden rounded-lg border border-slate-300 focus-within:border-brand-red">
              <div class="flex flex-wrap gap-1 border-b border-slate-200 bg-slate-50 p-2" role="toolbar" aria-label="正文格式">
                <button type="button" class="editor-button" title="段落" @mousedown.prevent @click="formatText('formatBlock', 'p')">段落</button>
                <button type="button" class="editor-button font-bold" title="加粗" @mousedown.prevent @click="formatText('bold')">B</button>
                <button type="button" class="editor-button italic" title="斜体" @mousedown.prevent @click="formatText('italic')">I</button>
                <button type="button" class="editor-button underline" title="下划线" @mousedown.prevent @click="formatText('underline')">U</button>
                <button type="button" class="editor-button" title="无序列表" @mousedown.prevent @click="formatText('insertUnorderedList')">• 列表</button>
                <button type="button" class="editor-button" title="有序列表" @mousedown.prevent @click="formatText('insertOrderedList')">1. 列表</button>
              </div>
              <div
                ref="editorRef"
                contenteditable="true"
                role="textbox"
                aria-multiline="true"
                aria-label="正文"
                data-placeholder="输入文章正文，可选中文字后设置格式"
                class="rich-editor min-h-[240px] max-h-[400px] overflow-y-auto px-4 py-3 text-sm leading-7 text-slate-700 outline-none"
                @input="syncEditor"
                @blur="syncEditor"
                @paste="pastePlainText"
              ></div>
            </div>
          </div>
          <label class="flex items-center gap-2 text-sm font-bold text-slate-700">
            <input v-model="form.is_published" type="checkbox" class="h-4 w-4 accent-brand-red" />
            立即发布（取消勾选则保存为草稿）
          </label>
          <p v-if="formError" class="text-sm text-brand-red">{{ formError }}</p>
          <div class="flex justify-end gap-3 pt-2">
            <button type="button" @click="closeEditor" class="rounded-lg border border-slate-300 px-5 py-2.5 text-sm font-bold text-slate-600 hover:bg-slate-100">取消</button>
            <button type="submit" :disabled="saving" class="btn-primary disabled:cursor-not-allowed disabled:opacity-60">
              {{ saving ? '保存中…' : '保存' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<style scoped>
.editor-button {
  padding: 0.375rem 0.75rem;
  border-radius: 0.375rem;
  color: #475569;
}
.editor-button:hover { background: #e2e8f0; }
.rich-editor {
  max-width: 100%;
  white-space: pre-wrap;
  overflow-wrap: anywhere;
  word-break: break-word;
}
.rich-editor:empty::before {
  content: attr(data-placeholder);
  color: #94a3b8;
  pointer-events: none;
}
.rich-editor :deep(p + p),
.rich-editor :deep(div + div) { margin-top: 0.5rem; }
.rich-editor :deep(ul),
.rich-editor :deep(ol) { padding-left: 1.5rem; }
.rich-editor :deep(ul) { list-style-type: disc; }
.rich-editor :deep(ol) { list-style-type: decimal; }
</style>