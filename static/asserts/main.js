var buttonContainer = document.querySelectorAll(
    ".tabContainer-Button button"
);
var tabpanel = document.querySelectorAll(".tabPanel");

function showPanel(indexPanel, bgcolor) {
    buttonContainer.forEach(function (node) {
        // console.log(node);
        node.classList.remove('tabButton');
        node.style.backgroundcolor = "";
        node.style.color = "";
    });
    buttonContainer[indexPanel].style.color = bgcolor;

    // node is a key word so we have to always use keywords
    tabpanel.forEach(function (node) {
        // console.log(node);
        // node.classList.remove('panelBackcss');
        node.style.display = 'none';
    });
    // hidebutton(tabpanel[indexPanel]);
    buttonContainer[indexPanel].classList.add('tabButton');
    tabpanel[indexPanel].style.display = 'grid'
    tabpanel[indexPanel].style.color = bgcolor;
    hidebutton();
}

function hidebutton() {
    tabpanel.forEach(function (node) {
        // console.log(node.style.display);
        if (node.style.display == 'grid') {
            var tabButton = document.querySelectorAll("#" + node.id + " a")
            var count = 0;
            tabButton.forEach(function (node) {
                if (count > 9) {
                    // node.style.display = 'none';
                    node.classList.remove('toggle-content.is-visible');
                    node.classList.add('toggle-content')
                    document.getElementById('hideShowButton').value = 'View More';
                }
                count++;
            })
        }
    });
}



function showButton() {
    console.log('-->', tabpanel);
    tabpanel.forEach(function (node) {
        // node.classList.remove('panelBackcss');
        if (node.style.display == 'grid') {
            var tabButton = document.querySelectorAll("#" + node.id + " a")
            var count = 0;
            tabButton.forEach(function (node) {
                if (count > 9) {
                    // node.style.display = 'block';
                    node.classList.remove('toggle-content');
                    node.classList.add('toggle-content.is-visible')
                    document.getElementById('hideShowButton').value = 'View Less';
                }
                count++;
            })
        }
    });
}

document.getElementById('hideShowButton').addEventListener('click', function () {
    var val = this.value;
    if (val == 'View More') {
        showButton();
    } else {
        hidebutton();
    }
})



showPanel(0, 'black')



// Product card  tab pannel
var buttonContainerProduct = document.querySelectorAll(
    ".ProductTabContainer .productTabContainer-Button button"
);
var tabpanelProduct = document.querySelectorAll(".productTabPanel");

// console.log(buttonContainerProduct);

function showPanelProduct(indexPanel, bgcolor) {
    buttonContainerProduct.forEach(function (node) {
        node.classList.remove('tabButton');
        node.style.backgroundcolor = "";
        node.style.color = "";
    });
    buttonContainerProduct[indexPanel].style.color = bgcolor;

    // node is a key word so we have to always use keywords
    tabpanelProduct.forEach(function (node) {
        // node.classList.remove('panelBackcss');
        node.style.display = 'none';
    });
    // tabpanelProduct[indexPanel].classList.add('panelBackcss');
    buttonContainerProduct[indexPanel].classList.add('tabButton');
    tabpanelProduct[indexPanel].style.display = 'grid'
    tabpanelProduct[indexPanel].style.color = bgcolor;
}

showPanelProduct(1, 'black')




// end of card tab pannel



// scroll event 

$(document).ready(function () {
    $(window).scroll(function () {
        let position = $(this).scrollTop();
        // console.log(position);
        var d = window.screen.availWidth;
        console.log(d);
        if (d > 800) {
            if (position > 320) {
                $('.formContanier').addClass('stickFormClass');
            } else {
                $('.formContanier').removeClass('stickFormClass');
            }
        }
    })
})

function openNav() {
    document.getElementById("mySidenav").style.width = "380px";
    document.getElementById("mySidenav").style.border = "1px solid black";
    $('body').addClass('offScroll');
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    $('body').removeClass('offScroll');
}
// end of scroll event