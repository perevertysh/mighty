<template>
    <div>        
        <b-form class="code-form">
          <label><h2> Напишите метод суммирующий два числа a и b</h2></label>
        <codemirror
            ref="cmEditor"
            :value="code"
            :options="cmOptions"
            @ready="onCmReady"
            @focus="onCmFocus"
            @input="onCmCodeChange"
        ></codemirror>
        <b-button 
          class="push-btn"
          v-on:click="pushAnswer()">
          Отправить
        </b-button>
          <b-spinner v-if="loadStatus" variant="secondary" label="Spinning"></b-spinner>
        </b-form>
    </div>
</template>

<script>
import rest from './../js/rest'
import 'codemirror/mode/python/python.js'
import 'codemirror/theme/base16-dark.css'

export default {
  props:{
    model:{
      type: String,
      default: 'answer',
    },
  },
  data () {
    return {
      code: "Введите код...",
      cmOptions: {
        tabSize: 4,
        mode: 'python',
        theme: 'base16-dark',
        lineNumbers: true,
        line: true,
      },
      loadStatus: false,
    }
  },
  methods: {
    onCmReady(cm) {
      console.log('the editor is readied!', cm)
    },
    onCmFocus(cm) {
      console.log('the editor is focused!', cm)
    },
    onCmCodeChange(newCode) {
      console.log('this is new code', newCode)
      this.code = newCode
    },

    checkSubmission(query){
      rest[this.model + "__check_submission"].post(query).then(res => 
      { 
        
        console.log("check_submission: " + query + ", response: " + res.data);
        
        if (typeof res.data === 'string')
        {
          this.codemirror.setValue(res.data);
          this.loadStatus = false;
          return;
        }else
        {
          setTimeout(()=>{this.checkSubmission(query)}, 100);
        };
      }).catch(err => 
      { 
        console.log("check_submission, Error: " + err);
        console.log(err);
      });  
    },

    pushAnswer: function(){

      console.log('start message sending...');
      let query = {"answer": this.codemirror.doc.getValue()};
      
      this.loadStatus = true;

      rest[this.model + "__add_submission"].post(query).then(res => 
      {
          let query = {};
          let evalStatus = res.data;
          
          console.log(evalStatus, typeof evalStatus);

          if (typeof evalStatus !== 'string'){
            
            query.id = evalStatus;
            
            console.log(query);

            this.checkSubmission(query);

          }else{
            this.codemirror.setValue(evalStatus);
            this.loadStatus = false;
          };
        
      }).catch(err => 
        { 
          console.log("add_sybmission:" + err)
        });
    }
  },
  computed: {
    codemirror() {
      return this.$refs.cmEditor.codemirror
    }
  },
  mounted() {
    console.log('the current CodeMirror instance object:', this.codemirror)
    // you can use this.codemirror to do something...
  }
}
</script>
