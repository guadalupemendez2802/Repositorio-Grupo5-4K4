import { useState } from 'react'
import landingPage from './componentes/landingPage'
import TicketsForm from './componentes/ticketsForm'
import './App.css'

function App() {
  const [pagina, setPagina] = useState('inicio')

  return (
    <div className="containerBox">
      {pagina === 'inicio' ? (
        <div className="tempDiv"></div>
        // <LandingPage onComprar={() => setPagina('formulario')} />
      ) : (
        <TicketsForm onVolver={() => setPagina('inicio')} />
      )}
    </div>
  )
}

export default App
