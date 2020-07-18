<template>
    <div class='main'>
        <b-container class="mb-4" fluid>
            <b-row align-h="start">
                <b-col class="filter_col" cols='4'>
                    <div class="filter-1">
                        <b-form inline  :style="{'justify-content': 'center'}" @reset="onReset">
                            <b-form inline v-for="(key, index) in filter_key" :key='index'>
                                <label 
                                    :for="'inline-form-input-' + key"
                                     class="mb-2 px-sm-4 mb-sm-0"
                                    :style="{
                                        'padding-right': '15px',
                                        'color':'#000000'
                                    }"
                                >{{filter[key].name}}</label>
                                <b-form-select
                                    :id="'inline-form-input-' + key"
                                    class="mb-2 px-sm-4 mb-sm-0"
                                    v-model='selectFilter[key]'
                                    :value-field='filter[key].value_field'
                                    text-field='name'
                                    :options='filter[key].items'
                                ></b-form-select>
                                <b-button
                                    class="mb-2 px-sm-4 mb-sm-0" 
                                    type="reset" @click="onReset()">
                                    Сбросить
                                </b-button>
                            </b-form>
                            
                        </b-form>
                    </div>
                </b-col>
                <b-col class="filter_col" cols='4'>
                    <div class="filter-1">
                        <b-form inline :style="{'justify-content': 'center'}">
                            <label
                                for="inline-form-input-sort"
                                :style="{
                                    'padding-right': '15px', 
                                    'color': '#000000'   
                                }"
                            >Сортировать по</label>    
                            <b-form-select
                                id="inline-form-input-sort"
                                class="mb-2 px-sm-4 mb-sm-0"
                                v-model='sortBy'
                                :options='optionsSort'
                            ></b-form-select>
                        </b-form>
                    </div>
                </b-col>
            </b-row>
        </b-container>
        <v-data-table  v-if="items && items.length"
            :headers="headers"
            :items="items"
            :items-per-page="perPage"
            :server-items-length="totalRows"
            :hide-default-footer="true"
            :sync-pagination="pagination"
            class="theme--dark text-xs-left v-data-table">
        </v-data-table>
        <div v-else class="empty" :style="{'margin-top': '15px'}">
            Задач нет
        </div>
        <b-pagination
            align="center"
            class="mx-2 mt-2"
            v-model="curPage"
            :total-rows="totalRows"
            :per-page="perPage"
            first-number
            last-number
        ></b-pagination>
    </div>
</template>

<script>
import rest from './../js/rest'
import AnswerCard from './answer_card'


export default {
    name: 'Answer',
    components: {
        AnswerCard,
    },
    props:{
        model: {
            type: String,
            default: 'answer',
        },
        search_str: {
            type: String,
            default: null,
        }
    },
    data: function() {
        return {
            headers: [
                 {
                    value: 'status.name', 
                    text: 'Статус ответа',
                },
                { 
                    value: 'id', 
                    text: 'Идентификатор ответа',
                    align: 'start',

                },
                {   
                    value: 'created_time', 
                    text: 'Время отправки'
                },
            ],
            items: null,
            sortBy: null,
            optionsSort: [
                {
                    value: 'status', 
                    text: 'статусу ответа',
                },
                {
                    value: '-status', 
                    text: 'статусу ответа(по убыванию)',
                },
                {
                    value: 'id', 
                    text: 'идентификатору ответа',
                },
                {
                    value: '-id', 
                    text: 'идентификатору ответа(по убыванию)',
                },
                {
                    value: 'created_time', 
                    text: 'времени отправки',
                },
                {
                    value: '-created_time', 
                    text: 'времени отправки(по убыванию)',
                }
            ],
            filter_key: ['status'],
            filter: {
                status: {
                    name: 'Статус ответа',
                    items: [],
                    value_field: 'code'
                }
            },
            selectFilter: {
                status: null
            },
            selectItem: null,
            countCol: 1,
            curPage: 1,
            perPage: 20,
            totalRows: 10,
        };
    },
    watch: {
        curPage () {
            this.fetch();    
        },
        sortBy (val, oldval) {
            this.fetch();
        },
        selectFilter: {
            handler() {
                this.fetch();
            },
            deep: true,
        },
        search_str: {
            handler(val) {
                this.$set(this.selectFilter, 'name', val);
            },
            deep: true,
        }
    },
    mounted: function() {
        this.fetch();
        this.loadFilters();
        console.log(this.search_str);
    },
    methods: {
        fetch() {
            let query = {page: this.curPage, page_size: this.perPage, ordering: this.sortBy};
            for (let key in this.filter) {
                let item = this.filter[key];
                query[key + '__' + item.value_field] = this.selectFilter[key];
            }
            query.search = this.selectFilter.name;
            query.status = this.selectFilter.status__code;
            rest[this.model].get(query).then(res => {
                if (res.data) {
                    this.items = res.data.results;
                    this.totalRows = res.data.count;
                }
            }). catch(err => {
                console.error(err);
            });
        },
        loadFilters() {
            for (let key in this.filter) {
                rest[key].get().then(res => {
                    this.filter[key].items = res.data.results;
                }).catch(err => {
                    console.error(err);
                });
            }
        },
        onReset() {
            for (let key in this.filter) {
                this.selectFilter[key] = null;
            }
        },
        changeStatus(status) {
            if (this.selectFilter.status == status) {
                this.selectFilter.status = null;
                return;
            }
            this.selectFilter.status = status;
        },
    }
}
</script>

