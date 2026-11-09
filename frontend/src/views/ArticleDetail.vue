<!-- src/views/ArticleDetail.vue -->
<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import http from '../api/http'
import { sanitizeRichText } from '../utils/richText'

interface Article {
  id: number
  title: string
  content: string
  summary: string | null
  created_at: string
  updated_at: string
}

const route = useRoute()
const router = useRouter()
const article = ref<Article | null>(null)
const loading = ref(true)
const notFound = ref(false)

function formatDate(iso: string) {
  return new Date(iso).toLocaleDateString('zh-CN', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  })
}

onMounted(async () => {
  try {
    const { data } = await http.get<Article>(`/articles/${route.params.id}`)
    article.value = data
  } catch {
    notFound.value = true
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <div class="min-h-screen bg-white">
    <header class="border-b border-slate-100">
      <div class="container-site flex items-center justify-between py-5">
        <a href="/" class="text-2xl font-black text-brand-navy">RUIPAI <span class="text-brand-red">瑞牌</span></a>
        <button
          @click="router.back()"
          class="inline-flex items-center gap-2 rounded-full border border-slate-300 px-5 py-2 text-sm font-bold text-slate-600 transition hover:bg-slate-100"
        >
          ← 返回
        </button>
      </div>
    </header>

    <main class="container-site py-14">
      <div v-if="loading" class="mx-auto max-w-3xl space-y-4">
        <div class="h-10 w-3/4 animate-pulse rounded bg-slate-100"></div>
        <div class="h-4 w-40 animate-pulse rounded bg-slate-100"></div>
        <div class="h-40 animate-pulse rounded bg-slate-100"></div>
      </div>

      <article v-else-if="article" class="mx-auto max-w-3xl">
        <p class="text-xs font-bold uppercase tracking-[0.3em] text-brand-red">BRAND NEWS</p>
        <h1 class="article-title mt-3 text-3xl font-black leading-tight text-brand-navy md:text-4xl">{{ article.title }}</h1>
        <p class="mt-4 text-sm text-slate-400">发布于 {{ formatDate(article.created_at) }}</p>
        <div class="mt-8 border-t border-slate-100 pt-8">
          <div class="article-body text-base leading-8 text-slate-700" v-html="sanitizeRichText(article.content)"></div>
        </div>
      </article>

      <div v-else-if="notFound" class="mx-auto max-w-xl rounded-2xl border border-dashed border-slate-300 py-20 text-center">
        <p class="text-2xl font-black text-brand-navy">文章不存在或已下架</p>
        <a href="/" class="mt-6 inline-flex items-center gap-2 font-bold text-brand-red hover:gap-4">← 返回首页</a>
      </div>
    </main>
  </div>
</template>
<style scoped>
.article-title,
.article-body {
  max-width: 100%;
  overflow-wrap: anywhere;
  word-break: break-word;
}

.article-body {
  white-space: pre-wrap;
}
.article-body :deep(p + p),
.article-body :deep(div + div),
.article-body :deep(p + ul),
.article-body :deep(p + ol) {
  margin-top: 1rem;
}
.article-body :deep(ul),
.article-body :deep(ol) {
  padding-left: 1.5rem;
}
.article-body :deep(ul) { list-style-type: disc; }
.article-body :deep(ol) { list-style-type: decimal; }
.article-body :deep(li + li) { margin-top: 0.25rem; }
</style>