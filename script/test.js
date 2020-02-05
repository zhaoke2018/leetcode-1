

// define tracer variables {
const tracer = new Array2DTracer('Knapsack Table');
const valuesTracer = new Array1DTracer('Values');
const weightsTracer = new Array1DTracer('Weights');
const logger = new LogTracer();
Layout.setRoot(new VerticalLayout([tracer, valuesTracer, weightsTracer, logger]));
tracer.set(DP);
valuesTracer.set(val);
weightsTracer.set(wt);
Tracer.delay();
// }




