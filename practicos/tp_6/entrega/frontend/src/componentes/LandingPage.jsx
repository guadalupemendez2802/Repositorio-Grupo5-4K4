import heroImg from '../assets/hero.png'

function LandingPage({ onComprar }) {
  return (
    <section id="center"> 
      <img src={heroImg} alt="Parque tematico" width={320} />
      <h1>Comprá tu entrada</h1>
      <p>Reservá tu visita al parque de forma rápida y segura.</p>
      <button type="button" className="btn-primary" onClick={onComprar}>
        Comprar entrada
      </button>
    </section>
  )
}

export default LandingPage