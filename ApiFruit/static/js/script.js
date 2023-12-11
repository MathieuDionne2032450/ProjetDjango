
(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
    // Loop over them and prevent submission
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
          if (!form.checkValidity()) {
            event.preventDefault()
            event.stopPropagation()
          }
  
          form.classList.add('was-validated')
        }, false)
      })
  })()


  function Prix (numero,id,quantite, prix){
    var newPrice = prix*quantite;
    console.log(id)
    $.ajax({url:"/ajout_quantite/"+id+"/"+quantite})
    document.getElementById("price_"+id).innerText = newPrice.toFixed(2)+"$";
    
    document.getElementById("prix_quantite_"+numero).value = newPrice.toFixed(2);

    $("#prix_total").text(PrixTotal()+"$");
   
    
  }

  function PrixTotal()
  {
    prixTotal = 0;
    for (i = 1; i <= $("#nbProduit").val(); i++) {
      prix = parseFloat(document.getElementById("prix_quantite_"+i).value);
      prixTotal += prix;
    }
    return prixTotal.toFixed(2);
  }

  $("#prix_total").ready(function (){
    $("#prix_total").text(PrixTotal()+"$");
  });