export {}
/**
 * The Builder interface specifies methods for creating the different parts of
 * the Product objects.
 */
interface Builder {
    producePartA(): void
    producePartB(): void
    producePartC(): void
}

/**
 * The Concrete Builder classes follow the Builder interface and provide
 * specific implementations of the building steps. Your program may have several
 * variations of Builders, implemented differently.
 */
class ConcreteBuilder1 implements Builder {
    #product: Product1

    /**
     * A fresh builder instance should contain a blank product object, which is
     * used in further assembly.
     */
    constructor() {
        this.reset()
    }

    public reset(): void {
        this.#product = new Product1()
    }

    /**
     * Concrete Builders are supposed to provide their own methods for
     * retrieving results. That's because various types of builders may create
     * entirely different products that don't follow the same interface.
     * Therefore, such methods cannot be declared in the base Builder interface
     * (at least in a statically typed programming language).
     *
     * Usually, after returning the end result to the client, a builder instance
     * is expected to be ready to start producing another product. That's why
     * it's a usual practice to call the reset method at the end of the
     * `getProduct` method body. However, this behavior is not mandatory, and
     * you can make your builders wait for an explicit reset call from the
     * client code before disposing of the previous result.
     */
    public getProduct(): Product1 {
        const result = this.#product
        this.reset()
        return result
    }
    /**
     * All production steps work with the same product instance.
     */
    public producePartA(): void {
        this.#product.parts.push("PartA1")    
    }

    public producePartB(): void {
        this.#product.parts.push("PartB1")
    }

    public producePartC(): void {
        this.#product.parts.push("PartC1")
    }
}

/**
 * It makes sense to use the Builder pattern only when your products are quite
 * complex and require extensive configuration.
 *
 * Unlike in other creational patterns, different concrete builders can produce
 * unrelated products. In other words, results of various builders may not
 * always follow the same interface.
 */
class Product1 {
    #parts: any[]

    constructor() {
        this.#parts = []
    }

    public get parts() {
        return this.#parts
    }

/**
 * The client code creates a builder object, passes it to the director and then
 * initiates the construction process. The end result is retrieved from the
 * builder object.
 */
/**
 * The client code creates a builder object, passes it to the director and then
 * initiates the construction process. The end result is retrieved from the
 * builder object.
 *//**
 * The client code creates a builder object, passes it to the director and then
 * initiates the construction process. The end result is retrieved from the
 * builder object.
 */

        public add(part: any): void {
        this.#parts.push(part)
    }

    public listParts(): void {
        console.log(`Product parts: ${this.#parts.toString()}`)
    }
} 

/**
 * The Director is only responsible for executing the building steps in a
 * particular sequence. It is helpful when producing products according to a
 * specific order or configuration. Strictly speaking, the Director class is
 * optional, since the client can control builders directly.
 */
class Director {
    #builder: Builder

    public get builder() {
        return this.#builder
    }

    /**
     * The Director works with any builder instance that the client code passes
     * to it. This way, the client code may alter the final type of the newly
     * assembled product.
     */
    public set builder(builder: Builder) {
        this.#builder = builder
    }

    /**
     * The Director can construct several product variations using the same
     * building steps.
     */
    public build_minimal_viable_product(): void {
        this.#builder.producePartA()
    }
    
    public build_full_viable_product(): void {
        this.#builder.producePartA()
        this.#builder.producePartB()
        this.#builder.producePartC()
    }
}

/**
 * The client code creates a builder object, passes it to the director and then
 * initiates the construction process. The end result is retrieved from the
 * builder object.
 */
function clientCode(director: Director): void {
    const builder = new ConcreteBuilder1()
    director.builder = builder

    console.log("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.getProduct().listParts()

    console.log("Standard full featured product: ")
    director.build_full_viable_product()
    builder.getProduct().listParts()

    console.log("Custom product: ")
    builder.producePartA()
    builder.producePartC()
    builder.getProduct().listParts()
}

const director = new Director()
clientCode(director)