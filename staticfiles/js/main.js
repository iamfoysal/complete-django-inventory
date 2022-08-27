


//csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

//index view from api

let productContainer = document.querySelector(".product-wrapper")
productContainer.innerHTML = ' '

function buildProduct(){

    let url = 'http://127.0.0.1:8000/api/'
    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
    console.log(data)

    let product = data
    for (let i in product){
        let products = `
        <div class="products-row" id='productId-${i}'>
        <button class="cell-more-button">
        <svg
            xmlns="http://www.w3.org/2000/svg"
            width="18"
            height="18"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="feather feather-more-vertical"
        >
            <circle cx="12" cy="12" r="1" />
            <circle cx="12" cy="5" r="1" />
            <circle cx="12" cy="19" r="1" />
        </svg>
        </button>
        <div class="product-cell image">
        <img
        src="${product[i].image}"
            alt="product"
        />
        <span>${ product[i].title }</span>
        </div>
        <div class="product-cell category">
        <span class="cell-label">Category:</span>${ product[i].category_name}
        </div>

        <div class="product-cell stock">
        <span class="cell-label">Stock:</span>${ product[i].stock }
        </div>

        <div class="product-cell price">
        <span class="cell-label">Price:</span>$ ${ product[i].price }
        </div>
        
        <div class="product-cell update-cell">
            <span class="cell-label">Details</span>
            <a href="/product/details/${product[i].id}/" class="update active"><i class="fa-solid fa-eye"></i></a>
        </div>

        <div class="product-cell update-cell">
        <span class="cell-label">Update</span>
        <!-- <span class="update active"
            ><i class="fa-solid fa-pen-to-square"></i
        ></span> -->
        <a href="/edit-product/${product[i].id}/" class="update active"
            ><i class="fa-solid fa-pen-to-square"></i
        ></a>
        </div>
        <div class="product-cell">
        <span class="cell-label">Delete:</span>
        <!-- <span class="delete"><i class="fa-solid fa-trash"></i></span> -->
        <a href="/delete-product/${product[i].id}" class="delete"><i class="fa-solid fa-trash"></i></a>
        </div>
    </div>
        ` 

        productContainer.innerHTML += products

    }

    })
}

buildProduct()


//add product api 
let productForm = document.getElementById('product-add-wrapper')

//console.log("=====v ssfs======")

productForm.addEventListener('submit', function(e){
    //let name = document.getElementById('id_title')
    e.preventDefault()
    //console.log(name.value)
    console.log("in product form submitted=======")
    
    // let url = 'http://127.0.0.1:8000/api/add/'

    // fetch(url, {
    //     method: 'POST',
    //     headers:{
    //         'Content-type': 'application/json',
    //         'X-CSRFToken' : csrftoken,
    //     },
    //     body: JSON.stringify({'title' : name})
    // })
})

console.log("in product form submitted=======")

