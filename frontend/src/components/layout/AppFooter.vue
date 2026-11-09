<!-- src/components/layout/AppFooter.vue -->
<script setup lang="ts">
const year = new Date().getFullYear()
const links = [
  { label: '关于亿鸿', href: '#about' }, { label: '研发实力', href: '#strength' },
  { label: '产品系列', href: '#products' }, { label: '品牌资讯', href: '#news' }, { label: '合作与荣誉', href: '#partners' }
]
</script>

<template>
  <footer id="contact" class="bg-brand-navy text-white">
    <div class="container-site grid gap-12 py-16 md:grid-cols-2 lg:grid-cols-3">
      <div><p class="text-2xl font-black">RUIPAI <span class="text-brand-red">瑞牌</span></p><p class="mt-3 text-sm text-slate-300">新护脊 · 选瑞牌</p><p class="mt-5 max-w-sm text-sm leading-7 text-slate-400">广州市亿鸿皮具有限公司，专注儿童书包研发、生产与销售，让每一次上学都轻松启程。</p></div>
      <div><h2 class="font-bold">快速导航</h2><nav class="mt-5 grid grid-cols-2 gap-3 text-sm text-slate-300" aria-label="页脚导航"><a v-for="link in links" :key="link.href" :href="link.href" class="hover:text-white">{{ link.label }}</a></nav></div>
      <div><h2 class="font-bold">联系合作</h2><p class="mt-5 text-sm leading-7 text-slate-300">欢迎品牌合作、产品咨询与渠道洽谈。</p><p class="mt-3 text-sm text-slate-300">所在地：中国 · 广州花都狮岭</p><p class="mt-3 text-sm text-slate-300">邮箱：19576407291@163.com</p></div>
    </div>
    <div class="border-t border-white/10"><div class="container-site flex flex-col gap-2 py-5 text-xs text-slate-400 md:flex-row md:justify-between"><p>© {{ year }} 广州市亿鸿皮具有限公司</p></div></div>
  </footer>
</template>
