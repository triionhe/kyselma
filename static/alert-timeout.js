setInterval( () => {
    Array.from(document.getElementsByClassName('kysAlert')).forEach( (a) => {
        a.addEventListener('click', (event) => { event.target.remove() } )
        if ( a.state == undefined ) a.state = 0
        if (a.state == 4) {
            a.style.transition = "opacity 1s"
            a.style.opacity = 0
        }
        if (a.state == 5) a.remove()
        a.state += 1
    } )
}, 1000)
