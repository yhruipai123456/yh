// src/router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AdminLogin from '../views/admin/AdminLogin.vue'
import AdminArticles from '../views/admin/AdminArticles.vue'
import ArticleDetail from '../views/ArticleDetail.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/news/:id', name: 'article-detail', component: ArticleDetail },
    { path: '/admin', name: 'admin-login', component: AdminLogin },
    {
      path: '/admin/articles',
      name: 'admin-articles',
      component: AdminArticles,
      meta: { requiresAuth: true },
    },
  ],
  scrollBehavior() {
    return { top: 0 }
  },
})

router.beforeEach((to) => {
  if (to.meta.requiresAuth && !localStorage.getItem('admin_token')) {
    return { name: 'admin-login' }
  }
  if (to.name === 'admin-login' && localStorage.getItem('admin_token')) {
    return { name: 'admin-articles' }
  }
})

export default router