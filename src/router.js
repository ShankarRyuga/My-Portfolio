import { createRouter, createWebHistory } from 'vue-router';
import About from './components/About.vue';
import Education from './components/Education.vue';
import Projects from './components/Projects.vue';
import Skills from './components/Skills.vue';
import Contact from './components/Contact.vue';

const routes = [
  { path: '/', component: About },
  { path: '/education', component: Education },
  { path: '/projects', component: Projects },
  { path: '/skills', component: Skills },
  { path: '/contact', component: Contact },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;