<template>
    <div :style='{display: "contents"}'>
        <b-navbar>
            <b-navbar-nav>
                <b-nav-form>
                    <b-button class="mx-2 header-btn" href='/app/answer'>Ответы</b-button>
                    <b-button class="mx-2 header-btn" href='/app/answer_checker'>Проверка</b-button>
                </b-nav-form>
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto">
                <b-nav-form>
                    <b-form-input
                        v-model='search_str'
                        size="sm"
                        class="mr-sm-2 search-form"
                        type='search'
                        placeholder="Найти задачу..."
                    />
                </b-nav-form>
            </b-navbar-nav>
        </b-navbar>
        <main class="main-content mt-2 mx-2">
            <router-view :search_str='search_str'/>
        </main>
    </div>
</template>

<script>
import AnswerMain from './answer_main'

export default {
    name: 'mainPage',
    components: {
        AnswerMain,
    },
    data: function() {
        return {
            search_str: null,
        };
    },
}
</script>