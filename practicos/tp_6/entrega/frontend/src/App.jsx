import { useState } from 'react'
import LandingPage from './componentes/LandingPage'
import TicketsForm from './componentes/ticketsForm'
import './App.css'

function App() {
  const [pagina, setPagina] = useState('inicio')

  return (
    <div className="containerBox">
      {pagina === 'inicio' ? (
        <LandingPage onComprar={() => setPagina('formulario')} />
      ) : (
        <TicketsForm onVolver={() => setPagina('inicio')} />
      )}
    </div>
  )
}

export default App
