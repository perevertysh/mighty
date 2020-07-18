<template>
    <div>
        <b-container fluid class="tail" v-if="item">
            <b-row key='info' id='info' align-h='around' sm="2">
                <b-col>
                {{item.id}}
                </b-col>
                <b-col>
                {{item.status.name}} 
                </b-col>
                <b-col>
                {{item.created_time}}
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
export default {
    name: 'AnswerCard',
    mixins: [
    ],
    props: {
        item: {
            default: null,
        },
        value: {
            type: Object,
            default: null,
        },
    },
    computed: {
    },
    methods: {
        select() {
            this.$router.push({name: 'answer.edit',  params: { id: this.item.id }});
        }
    }
}
</script>