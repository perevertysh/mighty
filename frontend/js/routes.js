import Vue from 'vue'
import VueRouter from 'vue-router'
import VueCodemirror from 'vue-codemirror'

Vue.use(VueRouter);

let routes = [];

import Answer from './../pages/answer_main'
import AnswerChecker from './../pages/answer_checker'



routes.push({
  path: "/answer_checker",
  component: AnswerChecker,
  name: 'answer-checker'
})

routes.push({
  path: "/answer",
  component: Answer,
  name: 'answer.list'
});

const router = new VueRouter({
  mode: 'history',
  base: 'app/',
  routes
})

router.beforeEach((to, from, next) => {
  if (to.path == '/') {
    next('/answer');
  }
  else {
    next();
  }
})
  
export {router};
