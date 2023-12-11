const kysLink = document.getElementById("kysLink")
kysLink.onclick = () => {
    const link = kysLink.innerHTML
    navigator.clipboard.writeText(link)
    const linkInfo = document.createElement("div")
    linkInfo.className = 'kysInfo'
    const linkText = document.createTextNode( 
            "Linkki " + link + " on kopioitu leikepöydälle." )
    linkInfo.appendChild( linkText )
    document.documentElement.lastChild.append(linkInfo)
}

setInterval( () => {
    Array.from(document.getElementsByClassName('kysInfo')).forEach( (a)=>{
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
