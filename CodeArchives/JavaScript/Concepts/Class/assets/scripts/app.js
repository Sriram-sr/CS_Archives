class Product {
  constructor(title, imageUrl, desc, price) {
    this.title = title;
    this.imageUrl = imageUrl;
    this.description = desc;
    this.price = price;
  }
}

class ElementAttribute {
  constructor(attrName, attrValue) {
    this.name = attrName;
    this.value = attrValue;
  }
}

class Componenent {
  constructor(renderHookId) {
    this.renderHook = document.getElementById(renderHookId);
  }
  createRootElement(tag, cssClasses, attributes) {
    const rootElement = document.createElement(tag);
    if (cssClasses) {
      rootElement.className = cssClasses;
    }
    if (attributes && attributes.length > 0) {
      for(const attrib of attributes) {
        rootElement.setAttribute(attrib.name, attrib.value);
      }
    }
    this.renderHook.appendChild(rootElement);
    
    return rootElement;
  }
}

class ShoppingCart extends Componenent {
  items = [];
  totalPrice = 0;

  constructor(renderHookId) {
    super(renderHookId);
  }

  addProduct(product) {
    this.items.push(product);   
    this.totalPrice+=product.price;
    this.totalOuput.innerHTML = `<h2>Total \$${this.totalPrice.toFixed(2)}</h2>`;
  }

  render() {
    const cartComponent = this.createRootElement('section', 'cart');
    cartComponent.innerHTML = `
    <h2>Total \$${0}</h2>
    <button>Order Now!</button>
    `;
    this.totalOuput = cartComponent.querySelector('h2');
  }
}

class ProductItem extends Componenent{
  constructor(product, renderHookId) {
    super(renderHookId);
    this.product = product;
  }

  addToCart() {
    App.addToCart(this.product);
  }

  render() {
    const productLiNode = this.createRootElement('li', 'product-item');
    productLiNode.innerHTML = `
        <div>
          <img src="${this.product.imageUrl}" alt="${this.product.title}" >
          <div class="product-item__content">
            <h2>${this.product.title}</h2>
            <h3>\$${this.product.price}</h3>
            <p>${this.product.description}</p>
            <button>Add to Cart</button>
          </div>
        </div>
      `;

    const addToCartButton = productLiNode.querySelector('button');
    addToCartButton.addEventListener('click', this.addToCart.bind(this));

    return productLiNode;
  }
}

class ProductList extends Componenent {
  products = [
    new Product(
      'A Pillow',
      'https://www.maxpixel.net/static/photo/2x/Soft-Pillow-Green-Decoration-Deco-Snuggle-1241878.jpg',
      'A soft pillow!',
      19.99
    ),
    new Product(
      'A Carpet',
      'https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Ardabil_Carpet.jpg/397px-Ardabil_Carpet.jpg',
      'A carpet which you might like - or not.',
      89.99
    ),
  ];

  renderProductItem() {
    const prodList = this.createRootElement('ul', 'product-list', [new ElementAttribute('id', 'prod-list')]);
    for (const product of this.products) {
      const productItem = new ProductItem(product, 'prod-list');
      const productListItem = productItem.render();
      prodList.appendChild(productListItem);
    }

    return prodList;
  }
}

class Shop {
  render() {
    this.cart = new ShoppingCart('app');
    this.cart.render();
    const product = new ProductList('app');
    product.renderProductItem();
  }
}

class App {
  static init() {
    const shopInstance = new Shop();
    shopInstance.render();
    this.cart = shopInstance.cart;
  }

  static addToCart(product) {
    this.cart.addProduct(product);
  }
}

App.init();