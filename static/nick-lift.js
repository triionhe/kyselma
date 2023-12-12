var nickTimeout
Array.from(document.getElementsByClassName('kysNick')).forEach( (a) => {
    a.addEventListener('mousedown', (event) => { nickTimeout = setTimeout( 
            () => { document.location = '/#nick_reset'}, 5000) })
    a.addEventListener('mouseup', (event) => { clearTimeout (nickTimeout) })
    a.addEventListener('mouseout', (event) => { clearTimeout (nickTimeout) })
})