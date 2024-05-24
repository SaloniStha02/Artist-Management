<template>
    <div class="min-h-screen flex">
      <Admindash />
      <div class="flex-grow p-6">
        <div class="bg-white rounded-lg p-6">
            <p class="text-3xl text-center my-10  text-lightblue">Song List</p>
          <table class=" w-2/3 border-collapse ml-64 mt-10">
            <thead>
              <tr class="border-4 border-purple text-xl text-center">
                <th class="p-3">ID</th>
                <th class="p-3">Title</th>
                <th class="p-3">Released Date</th>
                <th class="p-3">Artist Name</th>
                <th class="p-3 ">Actions</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="song in songs" :key="song.id" class="border-4 border-purple text-center">
                <td class="p-3">{{ song.id }}</td>
                <td class="p-3">{{ song.title }}</td>
                <td class="p-3">{{ song.released_date }}</td>
                <td class="p-3">{{ song.artist_name }}</td>
                <td class="p-3">
                  <button  @click="updateSong(song.id)"class="ring-2 ring-green hover:bg-green text-blackfont-bold py-2 px-4 rounded mr-2">Update</button>
                  <button  @click="deleteSong(song.id)"class="ring-2 ring-peach hover:bg-peach text-black  font-bold py-2 px-4 rounded">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
          <button @click="addSong" class="mt-5 ml-[77%] bg-purple py-3 px-3 rounded-lg">Add Song</button>
        </div>
      </div>
     
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import Admindash from './Admindash.vue';
  import { useRouter } from 'vue-router';
  const router = useRouter();
  const songs = ref([]);
  

  onMounted(async () => {
  try {
    const accessToken = localStorage.getItem('accessToken');
    const response = await axios.get('http://127.0.0.1:8000/songs/', {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    });
    songs.value = response.data;
  } catch (error) {
    console.error('Error fetching songs:', error);
  }
});
const updateSong=(id)=>{
    router.push({name:'Updatesong', params: { songId: id }});
}
const addSong=()=>{
    router.push({name:'Addsong'});
  }
const deleteSong = async (songId) => {
  const confirmation = window.confirm("Are you sure you want to delete this song?");
  if (confirmation) {
    try {
      const accessToken = localStorage.getItem('accessToken');
      const response = await axios.delete(`http://127.0.0.1:8000/songs/${songId}/`, {
        headers: {
          Authorization: `Bearer ${accessToken}`
        }
      });
      console.log('Song soft deleted successfully');
      songs.value = songs.value.filter(song => song.id !== songId);
    } catch (error) {
      console.error('Error soft deleting song:', error);
    }
  } else {
    console.log("Song deletion canceled");
  }
};
  </script>
  
  <style scoped>

  </style>
  