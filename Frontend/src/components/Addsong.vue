<template>
    <div class="min-h-screen bg-gray-100 flex flex-col">
     <nav class="bg-white shadow-md shawdow-purple w-full h-24">
       <div class=" mx-auto px-4 sm:px-6 lg:px-8">
         <div class="flex items-center justify-between h-full">
           <div class="flex items-center h-full">
             <img src="/public/logo.png" alt="Logo" class="w-16 mt-4">
           </div>
         </div>
       </div>
     </nav>
 
     <div class="flex flex-col md:flex-row items-center justify-around">
       <form class="bg-white border-2 border-lightblue w-6/12 h-4/5 mt-8 px-10 py-8 text-left shadow-md rounded-lg" @submit.prevent="addSong">
         <div class="grid grid-cols-2 gap-5">
           <div>
             <label class="block text-lg font-medium text-black mb-1">Title</label>
             <input type="text" name="title" id="fname" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="song.title" required>
           </div>
           <div>
             <label class="block text-lg font-medium text-black mb-1">Released Date</label>
             <input type="date" name="released_date" id="dob" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" v-model="song.released_date" required>
           </div>
            <div>
                <select v-model="song.artist" class="shadow-md w-full h-10 px-5 py-2 border-2 border-blue rounded-lg text-lg mb-5" required>
                <option v-for="artist in artists" :key="artist.id" :value="artist.id">{{ artist.name }}</option>
                </select>
            </div>
         <div class="flex justify-center">
           <button type="submit" class="ring-2 ring-purple rounded-lg px-4 py-2 text-black mr-12 mt-6">Add Song</button>
           <button @click="cancelSign" type="button" class="ring-2 ring-pink rounded-lg px-4 py-2 text-black mt-6">Cancel</button>
         </div>
        </div>
       </form>
     </div>
   </div>
 </template>
 <script setup>
  import axios from 'axios';
  import { useRouter } from 'vue-router';
  import { ref } from 'vue';
  import { useToast } from "vue-toastification";
  const toast = useToast({ position: 'bottom-left' });
 
  const song = ref({
      title: '',
      released_date: '',
      artist: '',
  });
  
  const router = useRouter();
 
  const addSong = () => {
    const accessToken = localStorage.getItem('accessToken');
    if (!accessToken) {
        console.error('No access token found');
        return;
    }

    axios.post('http://127.0.0.1:8000/songs/', {
       title:song.value.title,
       released_date:song.value.released_date,
       artist: song.value.artist
    }, {
        headers: {
            Authorization: `Bearer ${accessToken}`
        }
    })
    .then(response => {
        console.log("added song")
        router.push({ name: 'Allsongs' });
        toast.success("Song added ")
    })
    .catch(error => {
        console.error(error);
        toast.error("unsuccessful")
    });
};

  const cancelSign=()=>{
   router.push({name:'Allsongs'})
   toast.error (" canceled")

  }
  </script>
  
 