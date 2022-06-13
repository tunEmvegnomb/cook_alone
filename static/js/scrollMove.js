console.log('SCROLL 기동!')

function goToScroll(num) {
    // alert('SCROLL FUNCTION')
    if (num === 1) {
        let location = document.querySelector('.page2').offsetTop;
        window.scrollTo({top: location-100, behavior: 'smooth'});
    }
    else if (num===2) {
        let location = document.querySelector('.page3').offsetTop;
        window.scrollTo({top: location, behavior: 'smooth'});
    }
    else if (num===3) {
        let location = 0
        window.scrollTo({top: location, behavior: 'smooth'});
    }
}