Array.from(document.getElementsByClassName('kysAlert')).forEach( (a) => {
        a.addEventListener('click', (event) => {
            event.target.remove();
        })
        setTimeout( () => {
            Array.from(document.getElementsByClassName('kysAlert'))
                    .forEach( (a) => {
                if (a.style.transition=="opacity 2s") a.remove()
                a.style.transition="opacity 2s"
                a.style.opacity=0;
            } )
        }, 5000)
    })
