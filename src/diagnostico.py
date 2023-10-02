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
        self.declare(EstadoDiagnostico(nombre="posible_fiebre_detectada", diagnostico="indefinido"))
        

    @Rule(EstadoDiagnostico(nombre="posible_fiebre_detectada"), AND(Sintoma(dolor_de_garganta='s')))
    def regla2(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible faringitis"))
        #self.halt()

    @Rule(EstadoDiagnostico(nombre="posible_fiebre_detectada"), AND(Sintoma(dolor_de_garganta='n'), Sintoma(dolor_de_cabeza='s')))
    def regla3(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="posible_Posible gripe"))
        #self.halt()

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='n'), Sintoma(dolor_de_cabeza='s')))
    def regla4(self):
        self.declare(EstadoDiagnostico(nombre="posible_dolor_cabeza_detectado", diagnostico="indefinido"))
        

    @Rule(EstadoDiagnostico(nombre="posible_dolor_cabeza_detectado"), AND(Sintoma(congestion_nasal='s')))
    def regla5(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible resfriado común"))
        #self.halt()

    @Rule(EstadoDiagnostico(nombre="posible_dolor_cabeza_detectado"), AND(Sintoma(congestion_nasal='n'), Sintoma(tos='s')))
    def regla6(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible bronquitis"))
        #self.halt()

    @Rule(EstadoDiagnostico(nombre="inicial"), AND(Sintoma(fiebre='n'), Sintoma(dolor_de_cabeza='n'), Sintoma(congestion_nasal='s')))
    def regla7(self):
        self.declare(EstadoDiagnostico(nombre="posible_congestion_detectada", diagnostico="indefinido"))
        
    @Rule(EstadoDiagnostico(nombre="posible_congestion_detectada"), AND(Sintoma(tos='s')))
    def regla8(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible sinusitis"))
        #self.halt()

    @Rule(EstadoDiagnostico(nombre="posible_congestion_detectada"), AND(Sintoma(tos='n')))
    def regla9(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Posible alergia"))
        #self.halt()

    @Rule(EstadoDiagnostico(nombre="inicial"))
    def regla10(self):
        self.declare(EstadoDiagnostico(nombre="final", diagnostico="Síntomas no reconocidos"))
        #self.halt()

    def obtener_diagnostico(self):
        diagnosticos = []  
        #print(self.facts)
        for i in range(len(self.facts)):
            hecho = self.facts[i].as_dict()
            if hecho.get('nombre') == 'final':
                print(f"Estado diagnóstico: {hecho}")
                diagnosticos.append(hecho.get('diagnostico'))
            elif hecho.get('diagnostico') == 'indefinido' and hecho.get('nombre') != 'inicial':
                print(f"Estado diagnóstico: {hecho}")
                diagnosticos.append(hecho.get('nombre'))
        if len(diagnosticos) > 1:
            return ', '.join(diagnosticos[:-1])
        elif len(diagnosticos) == 1:
            return diagnosticos[0]
        else:
            print("Estado diagnóstico final no encontrado")
            return "Diagnóstico no encontrado"


