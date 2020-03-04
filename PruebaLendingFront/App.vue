<template>
    <div>
        <label for="businessInfo">Business Information: </label> 
        <div class="form-group">
             <label for="taxId">Tax Id: </label> 
             <input class="form-control" v-model="fTaxId" type="text" value="">
        </div>
                <div class="form-group">
             <label for="businessName">Business Name: </label> 
             <input class="form-control" v-model="fBusiName" type="text" value="">
        </div>
        <div class="form-group">
             <label for="businessAddress">Business Address: </label> 
             <input class="form-control" v-model="fBusiAddress" type="text" value="">
        </div>
        <div class="form-group">
             <label for="city">City: </label> 
             <input class="form-control" v-model="fCity" type="text" value="">
        </div>
                <div class="form-group">
             <label for="state">State: </label> 
             <input class="form-control" v-model="fState" type="text" value="">
        </div>
        <div class="form-group">
             <label for="postalCode">Postal Code: </label> 
             <input class="form-control" v-model="fPostCode" type="text" value="">
        </div>
        <div class="form-group">
             <label for="requestedAmount">Requested amount: </label> 
             <input class="form-control" v-model="fReqAmoun" type="text" value="">
        </div>
        <p></p>
             <label for="ownerInfo">Owner Information: </label>

        <div class="form-group">
             <label for="socialSecurityNumber">Social Security Number: </label> 
             <input class="form-control" v-model="fSoSecNum" type="text" value="">
        </div>
        <div class="form-group">
             <label for="name">Name: </label> 
             <input class="form-control" v-model="fName" type="text" value="">
        </div>
                <div class="form-group">
             <label for="email">Email: </label> 
             <input class="form-control" v-model="fEmail" type="text" value="">
        </div>
        <div class="form-group">
             <label for="address">Address: </label> 
             <input class="form-control" v-model="fAddress" type="text" value="">
        </div>
                <div class="form-group">
             <label for="owCity">City: </label> 
             <input class="form-control" v-model="fOwcity" type="text" value="">
        </div>
        <div class="form-group">
             <label for="owState">State: </label> 
             <input class="form-control" v-model="fOwState" type="text" value="">
        </div>
             <div class="form-group">
             <label for="postalCode">Postal Code: </label> 
             <input class="form-control" v-model="fOwPostCode" type="text" value="">
        </div>
        <p></p>

        <div class="form-group">
             <label for="loanDecision">loan decision: </label> 
             <input class="form-control" v-model="floanDecisi" type="text" value="" disabled>
        </div>
        
        <div>
            <button v-on:click="sendUserData" class="btn btn-success">Enviar</button>
            <button v-on:click="sendUserDataTornado" class="btn btn-success">EnviarTornado</button>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    export default {
        data(){
            return{
                todos: null,
                fTaxId:null,
                fBusiName:null,
                fBusiAddress:null,
                fCity:null,
                fState:null,
                fPostCode:null,
                fReqAmoun:null,
                fSoSecNum:null,
                fName:null,
                fEmail:null,
                fAddress:null,
                fOwcity:null,
                fOwState:null,
                fOwPostCode:null,
                floanDecisi:null
            }
        },
        mounted(){
            console.log("Hola Mundo mounted")
            this.getTodos();
        },
        methods: {
            getTodos(){
                console.log("in this place get all items of loan")
                axios.get('http://127.0.0.1:4000/requLoanList').then(response =>{
                //axios.get('https://jsonplaceholder.typicode.com/todos').then(response =>{
                    console.log(response.data)
                    console.log(response.data.requLoanList)
                    this.todos = response.data.requLoanList
                }).catch( e=> console.log(e)) 
            },
            sendUserData: function () {
                axios.post('http://127.0.0.1:4000/requLoanList', { 
                taxId: this.fTaxId,
                soSecNum: this.fSoSecNum,
                amount: this.fReqAmoun
                }, { useCredentails: true }).then(response => {
                // Respuesta del servidor
                this.floanDecisi=response.data.newRequLoan.loanDecis
                console.log(response);
                }).catch(e => {
                console.log(e); });
            },
            sendUserDataTornado: function () {

                axios.post('http://localhost:3000/api/itemD/', { 
                taxId: this.fTaxId,
                soSecNum: this.fSoSecNum,
                amount: this.fReqAmoun
                }, { useCredentails: true }).then(response => {
                // Respuesta del servidor
                this.floanDecisi=response.data.newRequLoan.loanDecis
                console.log(response);
                }).catch(e => {
                console.log(e); });
            }  
        }
    }
</script>

<style lang="scss" scoped>

</style>