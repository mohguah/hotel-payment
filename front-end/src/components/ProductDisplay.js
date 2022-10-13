import './ProductDisplay.scss';
import Peisestua from '../assets/images/peisestua.jpg';

const ProductDisplay = () => (
  <section>
    <div className="product">
      <img
        src={Peisestua}
        alt="The cover of Stubborn Attachments"
      />
      <div className="description">
        <h3>Peisestua</h3>
        <h5>1400 kr pr natt</h5>
      </div>
    </div>
    <div className='button-holder'>
      <form action="/create-checkout-session" method="POST">
        <button type="submit">
          Checkout
        </button>
      </form>
    </div>
  </section>
);

export default ProductDisplay