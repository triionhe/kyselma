var questions = {}

createQuestionDiv = ( question ) => {
    const questionDiv = document.createElement('div')
    questionDiv.className = 'kysQuestion'

    const qDiv = document.createElement('div')
    qDiv.appendChild( document.createTextNode( question.q ) )
    qDiv.className = 'kysText'
    questionDiv.appendChild( qDiv )
        
    const npDiv = document.createElement('div')
    npDiv.className = 'kysScale'

        const nDiv = document.createElement('div')
        nDiv.appendChild( document.createTextNode( question.n ) )
        nDiv.className = 'kysNegative'
        npDiv.appendChild( nDiv )
        
        const sDiv = document.createElement('div')
        sDiv.className = 'kysScaleSpacer'
        npDiv.appendChild( sDiv )

        const pDiv = document.createElement('div')
        pDiv.appendChild( document.createTextNode( question.p ) )
        pDiv.className = 'kysPositive'
        npDiv.appendChild( pDiv )

    questionDiv.appendChild( npDiv )

    const aDiv = document.createElement('input')
    aDiv.appendChild( document.createTextNode( question.a ) )
    aDiv.className = 'kysAnswer'
    aDiv.type = 'range'
    aDiv.min = 0
    aDiv.max = 999
    aDiv.disabled = true
    aDiv.value = question.a
    questionDiv.appendChild( aDiv )
    
    return questionDiv
}

createQuestions = () => {
    const questionsDiv = document.getElementById('questions')
    questionsDiv.className = 'kysQuestions'
    Object.keys(questions).forEach(k => { 
        questionsDiv.appendChild( createQuestionDiv( questions[k] ) )
    })
}

loadQuestions = async() => {
    await fetch( 'get/quiz_creator' )
        .then( response => response.json() )
        .then( json => questions = json )
        .catch( error => {
        alert("dkd")
        } )
    
    createQuestions()
}

loadQuestions()
