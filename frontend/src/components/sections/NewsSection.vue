<!-- src/components/sections/NewsSection.vue -->
<script setup lang="ts">
import { onMounted, ref } from 'vue'
import http from '../../api/http'

interface Article {
  id: number
  title: string
  content: string
  summary: string | null
  updated_at: string
}

const articles = ref<Article[]>([])
const loading = ref(true)

function formatDate(iso: string) {
  return new Date(iso).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

const allowedTags = new Set(['P', 'BR', 'STRONG', 'B', 'EM', 'I', 'U', 'UL', 'OL', 'LI', 'DIV', 'SPAN'])
const blockedTags = new Set(['SCRIPT', 'STYLE', 'IFRAME', 'OBJECT', 'EMBED', 'SVG', 'MATH', 'FORM', 'TEMPLATE'])

function renderPreview(item: Article) {
  const hasSummary = Boolean(item.summary)
  const source = item.summary || item.content
  const parsed = new DOMParser().parseFromString(source, 'text/html')
  const output = document.createElement('div')
  let remaining = hasSummary ? Infinity : 80
  let truncated = false

  function appendSafe(node: Node, parent: Node) {


    if (node.nodeType === Node.TEXT_NODE) {
      const text = hasSummary ? node.textContent || '' : (node.textContent || '').replace(/\s+/g, ' ')
      const safeText = text.slice(0, remaining)
      if (safeText) parent.appendChild(document.createTextNode(safeText))
      if (text.slice(safeText.length).trim()) truncated = true
      remaining -= safeText.length
      return
    }

    if (node.nodeType !== Node.ELEMENT_NODE) return
    const element = node as Element
    if (blockedTags.has(element.tagName)) return

    // Keep the text of unsupported formatting tags, but never copy their attributes.
    // Links are unwrapped because the entire news card is already a RouterLink.
    const safeElement = allowedTags.has(element.tagName) && remaining > 0
      ? document.createElement(element.tagName.toLowerCase())
      : parent
    if (safeElement !== parent) parent.appendChild(safeElement)
    element.childNodes.forEach((child) => appendSafe(child, safeElement))
  }

  parsed.body.childNodes.forEach((node) => appendSafe(node, output))
  if (!hasSummary && truncated) {
    output.appendChild(document.createTextNode('…'))
  }
  return output.innerHTML
}

onMounted(async () => {
  try {
    const { data } = await http.get<Article[]>('/articles')
    articles.value = data
  } catch {
    articles.value = []
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section id="news" class="section-pad bg-white">
    <div class="container-site">
      <div class="reveal flex flex-col justify-between gap-6 md:flex-row md:items-end">
        <div>
          <p class="section-kicker">05 / BRAND NEWS</p>
          <div class="eyebrow-line"></div>
          <h2 class="section-title">品牌资讯，<br />记录每一次出发</h2>
        </div>
        <p class="max-w-md text-sm leading-7 text-slate-600 md:text-base">了解企业动态与书包相关内容，持续更新。</p>
      </div>

      <div v-if="loading" class="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        <div v-for="n in 3" :key="n" class="h-56 animate-pulse rounded-2xl border border-slate-100 bg-slate-50"></div>
      </div>

      <div v-else-if="articles.length" class="mt-14 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        <RouterLink
          v-for="item in articles"
          :key="item.id"
          :to="{ name: 'article-detail', params: { id: item.id } }"
          class="group flex min-w-0 flex-col justify-between rounded-2xl border border-slate-100 bg-slate-50 p-6 transition hover:border-brand-red/40 hover:shadow-sm"
        >
          <div class="min-w-0">
            <p class="text-xs font-bold tracking-widest text-brand-red">{{ formatDate(item.updated_at) }}</p>
            <h3 class="news-title mt-3 text-xl font-black text-brand-navy group-hover:text-brand-red">{{ item.title }}</h3>
            <div class="news-rich-text mt-3 text-sm text-slate-600" v-html="renderPreview(item)"></div>
          </div>
          <p class="mt-5 inline-flex items-center gap-2 text-sm font-bold text-brand-red">
            阅读详情 <span aria-hidden="true" class="transition group-hover:translate-x-1">→</span>
          </p>
        </RouterLink>
      </div>

      <p v-else class="mt-14 rounded-2xl border border-dashed border-slate-300 py-16 text-center text-slate-400">
        暂无资讯，敬请期待
      </p>
    </div>
  </section>
</template>

<style scoped>
.news-title,
.news-rich-text {
  max-width: 100%;
  overflow-wrap: anywhere;
  word-break: break-word;
}

.news-rich-text {
  white-space: pre-wrap;
  line-height: 1.75;
}

.news-rich-text :deep(p + p),
.news-rich-text :deep(div + div),
.news-rich-text :deep(p + ul),
.news-rich-text :deep(p + ol) {
  margin-top: 0.5rem;
}

.news-rich-text :deep(ul),
.news-rich-text :deep(ol) {
  padding-left: 1.25rem;
}

.news-rich-text :deep(ul) { list-style-type: disc; }
.news-rich-text :deep(ol) { list-style-type: decimal; }
.news-rich-text :deep(li + li) { margin-top: 0.25rem; }
</style>
