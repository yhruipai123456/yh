<!-- src/components/sections/PartnersSection.vue -->
<script setup lang="ts">
const partners = ['Champion', 'BeLLE 百丽', 'TATA', 'POLO SPORT', 'Balabala', '学而思']
const honors = [
  { year: '2018', title: '参与儿童箱包相关标准起草' },
  { year: '2022', title: '1688 宝藏工厂 TOP100' },
  { year: '2023', title: '获高新技术企业称号' },
  { year: '品牌荣誉', title: '第十五届中国（狮岭）皮革皮具节最佳原创品牌奖' }
]
function hideBrokenImage(event: Event) { (event.target as HTMLImageElement).style.display = 'none' }
</script>

<template>
  <section id="partners" class="section-pad bg-slate-50"><div class="container-site"><div class="reveal text-center"><p class="section-kicker">06 / PARTNERS & HONORS</p><div class="eyebrow-line mx-auto"></div><h2 class="section-title">携手同行，<br />让每份信任都有回响</h2><p class="section-copy mx-auto mt-5 max-w-2xl">企业资料展示了多品牌合作与长期积累的行业荣誉。以下为资料中出现的部分合作品牌及荣誉。</p></div><div class="mt-14 grid grid-cols-2 gap-3 md:grid-cols-3 lg:grid-cols-6"><div v-for="name in partners" :key="name" class="reveal flex min-h-[100px] items-center justify-center rounded-xl border border-slate-200 bg-white px-3 text-center text-sm font-black text-slate-500 md:text-base">{{ name }}</div></div><div class="mt-20 grid gap-10 lg:grid-cols-2 lg:items-center"><div class="reveal relative min-h-[310px] overflow-hidden rounded-2xl bg-gradient-to-br from-slate-200 to-red-50 md:min-h-[420px]"><img :src="'/images/honor-wall.jpg'" alt="亿鸿皮具荣誉证书展示" class="absolute inset-0 h-full w-full object-contain" loading="lazy" @error="hideBrokenImage" /><div class="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-brand-navy/80 to-transparent p-8 text-white"><p class="text-xs tracking-[.2em]">HONORS & RECOGNITION</p><p class="mt-2 text-2xl font-bold">以长期积累，回应市场认可</p></div></div><div class="reveal"><p class="section-kicker">HONORS</p><h3 class="text-3xl font-black text-brand-navy">企业荣誉与行业参与</h3><ul class="mt-7 space-y-4"><li v-for="item in honors" :key="item.title" class="flex gap-4 border-b border-slate-200 pb-4"><span class="w-20 shrink-0 text-sm font-black text-brand-red">{{ item.year }}</span><span class="text-sm leading-6 text-slate-700">{{ item.title }}</span></li></ul><p class="mt-5 text-xs leading-6 text-slate-500"></p></div></div></div></section>
</template>
