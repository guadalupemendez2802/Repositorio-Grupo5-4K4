import logoImg from '../assets/logo_parque.png'
import { useNavigate } from "react-router-dom";

function LandingPage() {
  const navigate = useNavigate()
  return (
    <section id="center"> 
      <img src={logoImg} alt="Logo del Parque" width={320} />
      <h1>Comprá tu entrada</h1>
      <p>Reservá tu visita al parque de forma rápida y segura.</p>
      <button type="button" className="btn-primary" onClick={() => {navigate("/buy")}}>
        Comprar entrada
      </button>
    </section>
  )
}

export default LandingPage