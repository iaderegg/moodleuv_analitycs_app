function count(){
  var counter = { var: 0 };
  TweenMax.to(counter, 2, {
    var: 100,
    onUpdate: function () {
      var number = Math.ceil(counter.var);
      $('.counter').html(number);

    },
    ease:Circ.easeOut
  });
}

count();


// Bar chart courses by headquarters
new Chart(document.getElementById("courses-headquarters-bar-chart"), {
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
        text: 'Total de cursos por sede en el periodo actual'
      }
    }
});

// Bar chart users by headquarters
new Chart(document.getElementById("users-headquarters-bar-chart"), {
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
        text: 'Total de usuarios por sede en el periodo actual'
      }
    }
});

// Bar chart users by headquarters
new Chart(document.getElementById("courses-faculty-bar-chart"), {
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