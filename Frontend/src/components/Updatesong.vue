<template>
    <div class="min-h-screen flex flex-col ">
        <nav class="bg-white shadow-md w-full h-24">
      <div class=" mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-full">
          <div class="flex items-center h-full">
            <img src="/public/logo.png" alt="Logo" class="w-16 mt-4">
          </div>
        </div>
      </div>
    </nav>
  
  
      <div class="flex flex-col md:flex-row items-center justify-center">
        <form v-if="song"  @submit.prevent="updateSong"class="bg-white border-2 border-green-600 w-4/12 h-2/3 ml-1/2 mt-10 px-10 py-8  mr-20 text-left shadow-md rounded-lg">
          <div>
              <div>
                  <label class="block text-lg font-medium text-black mb-1">ID</label>
                  <input type="number" name="songId"class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="song.id"disabled>
              </div>
              <div>
                  <label class="block text-lg font-medium text-black mb-1">Title</label>
                  <input type="text" name="title"class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="song.title">
              </div>
              <div>
                  <label for="" class="block text-lg font-medium text-black mb-1">Released Date</label>
                  <input name="dob" type="date" class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="song.released_date">
              </div>
              <div>
                  <label for="" class="block text-lg font-medium text-black mb-1">Artist Name</label>
                  <textarea name="description" class="shadow-md w-full h-10 px-5 py-2 border-2 border-gray-300 rounded-lg text-lg mb-5" v-model="song.artist_name"></textarea>
              </div>
              <div class="flex justify-evenly">
                  <button class="rounded-lg ring-2 ring-lime-500 py-2 px-5 mt-6">Update</button>
                  <button class="rounded-lg ring-2 ring-red-500 py-2 px-5 mt-6" @click="cancelUpdate">Cancel</button>
              </div>
          </div>
      </form>
        </div>
    </div>

  </template>
<script setup>
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import axios from 'axios';

const route = useRoute();
const router = useRouter();
const songId = ref(route.params.songId);
const song = ref(null);

const fetchSong = async () => {
  const accessToken = localStorage.getItem('accessToken');
  try {
    const response = await axios.get(`http://127.0.0.1:8000/songs/${songId.value}/`, {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    });
    song.value = response.data;
  } catch (error) {
    console.error('Error fetching song:', error);
  }
};

const updateSong = async () => {
  const accessToken = localStorage.getItem('accessToken');
  try {
    const response = await axios.patch(`http://127.0.0.1:8000/songs/${songId.value}/`, {
      title: song.value.title,
      released_date: song.value.released_date,
      artist_name: song.value.artist_name,
    }, {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    });
    console.log('Song Updated', response.data);
    router.push({ name: 'Allsongs' });
  } catch (error) {
    console.error('Error updating song:', error);
  }
};

const cancelUpdate = () => {
  router.push({ name: 'Allsongs' });
};

onMounted(fetchSong);
</script>
