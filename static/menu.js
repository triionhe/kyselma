// menu.js - menu system for small site - 2022 Viljami Ilola

const jsonURL = 'pages.json'

var conf = {}
var pages = {}
var currentPage = null;
loadPages = async() => {
    await fetch( jsonURL )
        .then( response => response.json() )
        .then( json => conf = json )
        .catch( error => {
            document.body.innerHTML = `Error loading ${jsonURL}<hr>${error}` 
        } )
    pages = conf.pages
        
    installHamburger()
    createMenu()
    createPlaceholders()
    hashToPage()
}

createPlaceholders = () => {
    pagesMain = document.createElement('main')
    Object.keys(pages).forEach(p => {
        if ( pages[p].URL && pages[p].URL !== "" ) {
            const pageSection = document.createElement('section')
            pageSection.id = `${p}_page`
            pageSection.className='page'
            pagesMain.appendChild( pageSection )
        }
    })
    document.documentElement.lastChild.append( pagesMain )
}

createMenuIcon = (p) => {
    const icon = pages[p].menuIcon ? pages[p].menuIcon : ''
    if ( icon === '' ) return null

    const iconImg = document.createElement('img')
    iconImg.src = icon
            
    const iconAnchor = document.createElement('a')
    iconAnchor.href = `#${p}`
    iconAnchor.appendChild( iconImg )

    const iconDiv = document.createElement('div')
    iconDiv.className = 'menuIcon'
    iconDiv.appendChild( iconAnchor )
    
    return iconDiv
}

createMenuText = (p) => {
    const url = pages[p].URL ? pages[p].URL : ""
    const name = pages[p].menuName ? pages[p].menuName : url
    
    if ( name === '' ) return null
    
    const textNode = document.createTextNode( name )
            
    const textAnchor = document.createElement( url === "" ? 'div' : 'a')
    textAnchor.href = `#${p}`
    textAnchor.appendChild( textNode )

    const textDiv = document.createElement('div')
    textDiv.className = 'menuText'
    textDiv.appendChild( textAnchor )
    
    return textDiv
}

createMenu = () => {
    const menuNav = document.createElement('nav')
    menuNav.id = 'menu'
    menuNav.className = 'menuHidden'

    Object.keys(pages).forEach(p => {
    
        const entryDiv = document.createElement('div')
        entryDiv.className = 'menuItem'
        entryDiv.id = `${p}_menuEntry`

        const iconDiv = createMenuIcon(p)
        const textDiv = createMenuText(p)
        if ( iconDiv ) entryDiv.appendChild( iconDiv )
        if ( textDiv ) entryDiv.appendChild( textDiv )

        const url = pages[p].URL ? pages[p].URL : ""
        const name = pages[p].menuName ? pages[p].menuName : url
        if ( url === "" ) entryDiv.className += 
                name === "" ? ' menuSpacer' : ' menuTitle'
        else entryDiv.onclick = () => window.location.hash = p;

        if ( pages[p].hidden ) entryDiv.style.display = 'none';

        menuNav.append( entryDiv )
    })
    document.documentElement.lastChild.append( menuNav )
    
    const spacerDiv = document.createElement('div')
    spacerDiv.id = 'spaceBeforePage'
    document.documentElement.lastChild.append( spacerDiv )
}

installHamburger = () => {
    hamburgerDiv = document.createElement('div')
    hamburgerDiv.id = 'hamburgerMenu'
    hamburgerDiv.onclick = () => toggleMenu()	
    document.documentElement.lastChild.append( hamburgerDiv )
}

toggleMenu = () => {
    const menuNav = document.getElementById('menu')
    menuNav.className = menuNav.className === 'menuHidden' ? '' : 'menuHidden'
    if (menuNav.className === '') window.scrollTo(0,0)
}

hashToPage = async () => {
    const p = !document.location.hash
        ? Object.keys(pages)[0] : document.location.hash.substr(1) in pages
        ? document.location.hash.substr(1) : Object.keys(pages)[0]

    if ( p === Object.keys(pages)[0] ) {
        window.history.replaceState('', '', window.location.pathname)
    }
    if ( p === currentPage ) return false
    
    const pageElement = document.getElementById(`${p}_page`)

    if ( !currentPage ) currentPage = p;
    else document.getElementById(`${currentPage}_page`).className = 'page'
    pageElement.className = 'page pageActive'
    
    if ( pages[p].dynamic || !pageElement.loaded ) await fetch( pages[p].URL )
        .then( response => {
            if (!response.ok) return `ERROR loading "${pages[p].URL}"!`
            return response.text()
        } )
        .then( text => {
            pageElement.innerHTML = text;
            pageElement.loaded = true;
        } ) 
/*    if ( pageElement.innerHTML.startsWith("redirect = ") ) {
        pageElement.loaded = false;
        window.location.assign( pageElement.innerHTML.slice( 11 ) );
    }*/

    // https://plnkr.co/edit/MMegiu by Allen Kim
    Array.from(pageElement.querySelectorAll("script")).forEach(oldScript => {
        const newScript = document.createElement("script");
        Array.from(oldScript.attributes).forEach(attr =>
                newScript.setAttribute(attr.name, attr.value));
        newScript.appendChild(document.createTextNode(oldScript.innerHTML));
        oldScript.parentNode.replaceChild(newScript, oldScript);
    });

    document.getElementById(`${currentPage}_menuEntry`)
        .className = 'menuItem'
    document.getElementById(`${p}_menuEntry`)
        .className = 'menuItem menuItemActive'
    currentPage = p
    if (!pages[p].pageTitle) document.title = conf.title
    else document.title = `${pages[p].pageTitle} - ${conf.title}`    
}

hideMenu = () => document.getElementById('menu').className = 'menuHidden';

window.onload = async() => {
    loadPages()
}
window.onhashchange = () => {
    hideMenu()
    hashToPage()
}
