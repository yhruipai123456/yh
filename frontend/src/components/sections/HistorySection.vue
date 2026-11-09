<!-- src/components/sections/HistorySection.vue -->
<script setup lang="ts">
const milestones = [
  { year: '1992', title: '创业起步', text: '品牌创始人黄海涛南下创业，开启皮具事业。' },
  { year: '2007', title: '创牌建厂', text: '聚焦学生书包，注册 RUIPAI 商标，自建工厂。' },
  { year: '2013', title: '布局电商', text: '进入天猫、阿里、京东等线上平台。' },
  { year: '2018', title: '持续发展', text: '拓展产能，并参与儿童箱包相关标准起草。' },
  { year: '2024', title: '品牌升级', text: '围绕新一代护脊书包持续升级产品与传播。' },
  { year: '2025', title: '探索海外', text: '企业资料记载了拓展全球渠道的规划。' }
]
</script>

<template>
  <section id="history" class="section-pad bg-slate-50"><div class="container-site"><div class="reveal max-w-2xl"><p class="section-kicker">02 / OUR JOURNEY</p><div class="eyebrow-line"></div><h2 class="section-title">一程一印记，<br />向未来持续前行</h2><p class="section-copy mt-6">从创业起步到品牌升级，每一步都围绕儿童书包展开。</p></div><ol class="mt-14 grid gap-4 md:grid-cols-2 lg:grid-cols-3"><li v-for="item in milestones" :key="item.year" class="reveal relative min-h-[210px] rounded-2xl border border-slate-200 bg-white p-7 shadow-sm"><span class="absolute right-6 top-5 text-5xl font-black text-slate-100">{{ item.year }}</span><div class="relative"><p class="text-sm font-black tracking-widest text-brand-red">{{ item.year }}</p><h3 class="mt-8 text-xl font-bold text-brand-navy">{{ item.title }}</h3><p class="mt-3 text-sm leading-7 text-slate-600">{{ item.text }}</p></div></li></ol></div></section>
</template>
