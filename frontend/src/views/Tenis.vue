<template>
    <div>
        <h2>
            Tenistas no inscritos
        </h2>
    </div>
    <div id = "tenista-list">
        <input v-model="edicion" type ="number" placeholder="Pon el número de la edición">
        <ul>
            <li v-for="tenis in tenistas"<{{ tenis }} </li>
        </ul>
    </div>
</template>

<script>
import axios from 'axios';

export default{ 
    data(){
        return  {
                    tenistas: [],
                    errores: [],
        }
    },
    {
        
    }
}
</script>
