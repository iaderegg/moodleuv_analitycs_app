$(document).ready(function(){

    $.ajax({
        url: '/get_general_summary/',
        dataType: 'json',
        type: 'POST',
        data: {
          'init_year': 0
        },
        success: function(data) {

            if (data.is_valid) {
              // Cursos
              count(data.total_courses_uv, $('#counter-total-courses'))
              count(data.total_courses_current_year_uv, $('#counter-courses-current-semester'))
              count(data.total_regular_courses, $('#counter-regular-courses'))
              count(data.total_no_regular_courses, $('#counter-no-regular-courses'))

              var coursesByHeadquarter = JSON.parse( data.courses_by_headquarter )
              var coursesByFaculties = JSON.parse( data.courses_by_faculties )

              // Bar chart courses by headquarters
              new Chart(document.getElementById("courses-headquarters-bar-chart"), {
                type: 'bar',
                data: {
                  labels: coursesByHeadquarter['headquarters'],
                  datasets: [
                    {
                      label: "Cursos",
                      backgroundColor: "#3e95cd",
                      data: coursesByHeadquarter['total'],
                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                    text: 'Total de cursos por sede en el año seleccionado'
                  }
                }
              });

              // Bar chart courses by faculties
              new Chart(document.getElementById("courses-faculty-bar-chart"), {
                type: 'bar',
                data: {
                  labels: coursesByFaculties['faculties'],
                  datasets: [
                    {
                      label: "Cursos",
                      backgroundColor: "#8e5ea2",
                      data: coursesByFaculties['total'],
                    }
                  ]
                },
                options: {
                  legend: { display: false },
                  title: {
                    display: true,
                    text: 'Total de cursos por facultad en el año seleccionado'
                  }
                }
              });

              // Usuarios
              count(data.total_users_uv, $('#counter-total-users'))
            } else {
              console.log("Ajax error")
            }
        },
        error: function(e){
            console.log(e);
        }
    });
})

// Función que da animación a cifras numéricas
function count(number, element){
  var counter = { var: 0 };
  TweenMax.to(counter, 2, {
    var: number,
    onUpdate: function () {
      var number = Math.ceil(counter.var);
      $(element).html(number);

    },
    ease:Circ.easeOut
  });
}

//Django basic setup for accepting ajax requests.
// Cookie obtainer Django

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
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

// Setup ajax connections safetly

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});






// Bar chart users by headquarters
new Chart(document.getElementById(""), {
    type: 'bar',
    data: {
      labels: ["Melendéz", "San Fernando", "Palmira", "Tulúa", "Norte del Cauca"],
      datasets: [
        {
          label: "Cursos",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: [2478,5267,734,784,433]
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Total de usuarios por facultad o instituto en el periodo actual'
      }
    }
});

// Bar chart users by headquarters
new Chart(document.getElementById("users-faculty-bar-chart"), {
    type: 'bar',
    data: {
      labels: ["Melendéz", "San Fernando", "Palmira", "Tulúa", "Norte del Cauca"],
      datasets: [
        {
          label: "Cursos",
          backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
          data: [2478,5267,734,784,433]
        }
      ]
    },
    options: {
      legend: { display: false },
      title: {
        display: true,
        text: 'Total de usuarios por facultad o instituto en el periodo actual'
      }
    }
});