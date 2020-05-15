var movies=[];
var movie_count=0;
function getCatalog(){
    $.ajax({
        url:'http://127.0.0.1:8000/api/movies',
        type:"GET",
        success:function(response){
            console.log("response from server",response);
            movies=response.objects;
            movie_count=0;

            for(var i=0; i<movies.length;i++){
                var movie=movies[i];
                displayMovie(movie);
            }
        },
        error:function(errorDetails){
            console.log("Error",errorDetails);
        }
    })
}

function displayMovie(movie){
    // get container
    var Container=$('#movies_container');

    var first="active";
  if(movie_count>0){
      first="";
  }

    //create html sintax
    var NewMovie=`<div class="carousel-item ${first}">
    <img src="${movie.image_url}" class="d-block w-100" alt="...">
    <div class="carousel-caption">
      <div class="card bg-light" style="color:black;">
    <h5>${movie.title}</h5>
      <p> Genre: ${movie.genre.name} Year: ${movie.release_year} , Star: ${movie.star} </p>
      </div>
    </div>
  </div>`;

  

    var Indicator=`<li data-target="#carouselExampleCaptions" data-slide-to="${movie_count}" class="${first}"></li>`

  

    //add sintax to container

    $('#movies_container').append(NewMovie);
    $('#movies_indicators').append(Indicator);
    movie_count++;

}

function init(){
    console.log("Catalog JS is loaded");
    getCatalog();
}

window.onload=init;