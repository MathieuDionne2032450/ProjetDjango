(function () {
    'use strict'
  
    // Fetch all the forms we want to apply custom Bootstrap validation styles to
    var forms = document.querySelectorAll('.needs-validation')
    console.log("test")
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

  var prixTotal = 0
  var prixProd = 0

  function Prix (count,id,quantite, prix){
    var newPrice = prix*quantite;
    document.getElementById("price_"+id).innerText = newPrice.toFixed(2)+"$";
    document.getElementById("prix_quantite_"+id).value = newPrice.toFixed(2);
    PrixTotal(id,count)
  }

  function PrixTotal(id,countProduit)
  {
    for (i = 0; i < countProduit; i++) {
      prixTotal = document.getElementById("prix_quantite_"+i).value;
    }
    
    document.getElementById("prix_total").innerText = prixTotal.toFixed(2)+"$";
  }