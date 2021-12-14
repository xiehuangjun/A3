const RegForm =  document.getElementById("RegForm");
RegForm.addEventListener('submit', function (e) {             // Confirm whether the button click or not 
    e.preventDefault();

    var formdata = new FormData(document.getElementById('RegForm'));      // Creating a new formdata and listen the value of the form which named myForm in HTML
    fetch("http://IP:5000/register",{
            method: 'POST',
            body: formdata
        })
        .then(response => {return response.json()})
        .then(function(myJson){
            console.log(myJson);
            if(myJson.Log == "Register Success"){
                swal('Success', 'Register Successfully', 'success', {timer: 2000});
                var delayInMilliseconds = 1000;
                setTimeout(function() {
                    //window.sessionStorage.setItem("Useraccount",account);
                    window.location.replace('login.html');
                }, delayInMilliseconds);
            }else if(myJson.Log== "Account already used" ){
                swal('Fail', 'Register fail', 'error')
            }
        }) 
        //   .then( (data) =>{render(data)})                 // Getting response then call function to do something
});

