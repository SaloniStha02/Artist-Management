 import './assets/style.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './route'
import axios from 'axios'
import Toast from 'vue-toastification'
import 'vue-toastification/dist/index.css'
axios.defaults.baseURL=''
const app = createApp(App)

app.use(router)
app.use(Toast)
app.mount('#app')
