Array.from(document.getElementsByClassName('kysAlert')).forEach( (a) => {
        a.addEventListener('click', (event) => {
            event.target.remove();
        })
    })
