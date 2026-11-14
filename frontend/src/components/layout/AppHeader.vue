<!-- src/components/layout/AppHeader.vue -->
<script setup lang="ts">
import { ref } from 'vue'

const open = ref(false)
const links = [
  { label: '首页', href: '#home' }, { label: '关于亿鸿', href: '#about' },
  { label: '发展历程', href: '#history' }, { label: '研发实力', href: '#strength' },
  { label: '产品系列', href: '#products' },{ label: '品牌资讯', href: '#news' }, { label: '合作与荣誉', href: '#partners' },
]
function closeMenu() { open.value = false }
</script>

<template>
  <header class="sticky top-0 z-50 border-b border-slate-200/80 bg-white/95 shadow-sm backdrop-blur">
    <div class="container-site flex h-[72px] items-center justify-between gap-5">
      <a href="#home" class="flex shrink-0 items-center gap-3" aria-label="亿鸿皮具，返回首页" @click="closeMenu">
        <img src="/logo.png" alt="亿鸿皮具 RUIPAI 瑞牌 新一代护体书包" class="h-12 w-auto object-contain" />
      </a>
      <nav class="hidden items-center gap-6 lg:flex" aria-label="主导航">
        <a v-for="link in links" :key="link.href" :href="link.href" class="text-sm font-semibold text-slate-700 transition hover:text-brand-red">{{ link.label }}</a>
      </nav>
      <a href="#contact" class="hidden rounded-full bg-brand-red px-5 py-2.5 text-sm font-bold text-white transition hover:bg-red-700 md:inline-flex">联系合作</a>
      <button type="button" class="inline-flex h-11 w-11 items-center justify-center rounded-lg border border-slate-200 text-2xl lg:hidden" :aria-expanded="open" aria-controls="mobile-nav" aria-label="切换导航菜单" @click="open = !open">{{ open ? '×' : '☰' }}</button>
    </div>
    <nav v-if="open" id="mobile-nav" class="border-t border-slate-100 bg-white px-5 pb-5 lg:hidden" aria-label="移动端导航">
      <a v-for="link in links" :key="link.href" :href="link.href" class="block border-b border-slate-100 py-3 text-sm font-semibold" @click="closeMenu">{{ link.label }}</a>
      <a href="#contact" class="mt-4 block text-sm font-bold text-brand-red" @click="closeMenu">联系合作 →</a>
    </nav>
  </header>
</template>
