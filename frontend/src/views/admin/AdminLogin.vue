<!-- src/views/admin/AdminLogin.vue -->
<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import http from '../../api/http'

const router = useRouter()
const username = ref('')
const password = ref('')
const loading = ref(false)
const error = ref('')

async function onSubmit() {
  if (!username.value || !password.value) {
    error.value = '请输入用户名和密码'
    return
  }
  loading.value = true
  error.value = ''
  try {
    const form = new URLSearchParams()
    form.append('username', username.value)
    form.append('password', password.value)
    const { data } = await http.post('/auth/login', form, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    })
    localStorage.setItem('admin_token', data.access_token)
    router.push('/admin/articles')
  } catch (e: any) {
    error.value = e?.response?.data?.detail ?? '登录失败，请重试'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="flex min-h-screen items-center justify-center bg-slate-100 px-5">
    <div class="w-full max-w-sm rounded-2xl bg-white p-8 shadow-sm">
      <div class="mb-8 text-center">
        <p class="text-xs font-bold uppercase tracking-[0.3em] text-brand-red">YIHONG ADMIN</p>
        <h1 class="mt-2 text-2xl font-black text-brand-navy">后台登录</h1>
      </div>
      <form class="space-y-4" @submit.prevent="onSubmit">
        <div>
          <label class="mb-1 block text-sm font-bold text-slate-700" for="username">用户名</label>
          <input
            id="username"
            v-model="username"
            type="text"
            autocomplete="username"
            class="w-full rounded-lg border border-slate-300 px-4 py-2.5 text-sm outline-none transition focus:border-brand-red"
            placeholder="请输入用户名"
          />
        </div>
        <div>
          <label class="mb-1 block text-sm font-bold text-slate-700" for="password">密码</label>
          <input
            id="password"
            v-model="password"
            type="password"
            autocomplete="current-password"
            class="w-full rounded-lg border border-slate-300 px-4 py-2.5 text-sm outline-none transition focus:border-brand-red"
            placeholder="请输入密码"
          />
        </div>
        <p v-if="error" class="text-sm text-brand-red">{{ error }}</p>
        <button
          type="submit"
          :disabled="loading"
          class="btn-primary w-full disabled:cursor-not-allowed disabled:opacity-60"
        >
          {{ loading ? '登录中…' : '登录' }}
        </button>
      </form>
      <p class="mt-6 text-center text-xs text-slate-400">
        <a href="/" class="hover:text-brand-red">← 返回官网</a>
      </p>
    </div>
  </div>
</template>