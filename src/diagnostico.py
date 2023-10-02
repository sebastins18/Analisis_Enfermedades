from experta import KnowledgeEngine, Fact, Rule, AND, DefFacts

class Sintoma(Fact):
    pass

class EstadoDiagnostico(Fact):
    pass

class Diagnostico(KnowledgeEngine):
    
    @DefFacts()
    def _initial_facts(self):
        yield EstadoDiagnostico(nombre="inicial", diagnostico="indefinido")

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='s')))
    def regla1(self):
        self.declare(EstadoDiagnostico(nombre="fiebre_detectada", diagnostico="indefinido"))
        

    @Rule(EstadoDiagnostico(nombre="fiebre_detectada"), AND(Sintoma(dolor_de_garganta='s')))
    def regla2(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible faringitis"))
        self.halt()

    @Rule(EstadoDiagnostico(nombre="fiebre_detectada"), AND(Sintoma(dolor_de_garganta='n'), Sintoma(dolor_de_cabeza='s')))
    def regla3(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible gripe"))
        self.halt()

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='n'), Sintoma(dolor_de_cabeza='s')))
    def regla4(self):
        self.declare(EstadoDiagnostico(nombre="dolor_cabeza_detectado", diagnostico="indefinido"))
        

    @Rule(EstadoDiagnostico(nombre="dolor_cabeza_detectado"), AND(Sintoma(congestion_nasal='s')))
    def regla5(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible resfriado común"))
        self.halt()

    @Rule(EstadoDiagnostico(nombre="dolor_cabeza_detectado"), AND(Sintoma(congestion_nasal='n'), Sintoma(tos='s')))
    def regla6(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible bronquitis"))
        self.halt()

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='n'), Sintoma(dolor_de_cabeza='n'), Sintoma(congestion_nasal='s')))
    def regla7(self):
        self.declare(EstadoDiagnostico(nombre="congestion_detectada", diagnostico="indefinido"))
        

    @Rule(EstadoDiagnostico(nombre="congestion_detectada"), AND(Sintoma(tos='s')))
    def regla8(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible sinusitis"))
        self.halt()

    @Rule(EstadoDiagnostico(nombre="congestion_detectada"), AND(Sintoma(tos='n')))
    def regla9(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible alergia"))
        self.halt()

    @Rule(EstadoDiagnostico(nombre="inicial"))
    def regla10(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Síntomas no reconocidos"))
        self.halt()

    def obtener_diagnostico(self):
        for i in reversed(range(len(self.facts))):
            hecho = self.facts[i].as_dict()
            if hecho.get('nombre') == 'final':
                print(f"Estado diagnóstico final: {hecho}")
                return hecho.get('diagnostico')
        print("Estado diagnóstico final no encontrado")
        return "Diagnóstico no encontrado"