import React from 'react'
import ReactDOM from 'react-dom/client'
import './scss/main.css'
import Section_1 from './components/Section_1'
import Section_2 from './components/Section_2'
import Section_3 from './components/Section_3'
import Section_4 from './components/Section_4'
import Section_5 from './components/Section_5'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <Section_1/>
    <Section_2/>
    <Section_3/>
    <Section_4/>
    <Section_5/>
  </React.StrictMode>
)
