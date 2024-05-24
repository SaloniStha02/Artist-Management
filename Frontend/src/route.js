import{createWebHistory,createRouter} from 'vue-router';
import Login from './components/Login.vue';
import Signup from './components/Signup.vue';

import Admindash from './components/Admindash.vue';
import Artdash from './components/Artdash.vue';

import Allsongs from './components/Allsongs.vue';
import Addart from './components/Addart.vue';
import Allartist from './components/Allartist.vue';
import Adminpro from './components/Adminpro.vue';
import Updateart from './components/Updateart.vue';
import Artistpro from './components/Artistpro.vue';
import Updatesong from './components/Updatesong.vue';
import Addsong from './components/Addsong.vue';

import Updatepro from './components/Updatepro.vue';
const routes=[
    
    {
        name:'Login',
        path :'/',
        component: Login
    },
    {
        name:'Signup',
        path :'/signup',
        component: Signup
    },
    {
        name:'Admindash',
        path :'/admin-dash',
        component: Admindash
    },
    {
        name:'Allsongs',
        path :'/allsongs',
        component: Allsongs
    },
    {
        name:'Allartist',
        path :'/allartist',
        component: Allartist
    },
    {
        name:'Adminpro',
        path :'/admin-profile',
        component: Adminpro
    },
    {
        name:'Updateart',
        path:'/user/:artistId',
        component:Updateart,
    
    },
    {
        name:'Artistpro',
        path:'/artist-profile',
        component:Artistpro,
    
    },
    {
        name:'Addart',
        path:'/create-artist',
        component:Addart,
    
    },
    {
        name:'Updatesong',
        path:'/song/:songId',
        component:Updatesong,
    
    },
    {
        name:'Addsong',
        path:'/create-song',
        component:Addsong,
    
    },
    {
        name:'Artdash',
        path :'/artist-dash',
        component: Artdash
    },
    {
        name:'Updatepro',
        path:'/user/:artistId',
        component:Updatepro,
    
    },
    ];

const router=createRouter({
    history:createWebHistory(),
    routes
});

export default router;