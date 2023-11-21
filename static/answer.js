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

    const aInput = document.createElement('input')
    aInput.className = 'kysAnswer'
    aInput.type = 'range'
    aInput.min = 0
    aInput.max = 999
    aInput.value = 500
    aInput.name = question.i
    questionDiv.appendChild( aInput )
    
    return questionDiv
}

createQuestions = () => {
    const kysForm = document.getElementById('questionForm')
    const questionsDiv = document.createElement('div')
    Object.keys(questions).forEach(k => { 
        questionsDiv.appendChild( createQuestionDiv( questions[k] ) )
    })
    kysForm.appendChild( questionsDiv )
    const submitInput = document.createElement('input')
    submitInput.type='submit'
    submitInput.value='Vastaa kyselyyn'
    submitInput.className = 'kysSubmitAnswers'
    kysForm.appendChild( submitInput )
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
