import { createRouter, createWebHashHistory } from 'vue-router'
import CreateProject from '../views/CreateProject.vue'
import MainApp from '../views/MainApp.vue'
import FeatureExtraction from '../views/FeatureExtraction.vue'

const routes = [
  {
    path: '/',
    name: 'createProject',
    component: CreateProject
  },
  {
    path: '/mainapp/:id/:filePath/:fileName',
    name: 'mainApp',
    props: true,
    component: MainApp
  },
  {
    path: '/feauextraction',
    name: 'featureExtraction',
    component: FeatureExtraction
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
