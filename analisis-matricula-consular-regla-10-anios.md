# Matrícula consular del inmigrante y la regla de los 10 años

**Fecha:** 2026-09-17
**Fuentes:** índice alfabético de matrículas de Chile (consulado de Santiago) y volúmenes digitalizados del
Politisches Archiv des Auswärtigen Amts (PA AA). Imágenes en
`01-Friedrich-Wilhelm-August-Vermehren/matricula-consular/`.

## 1. Qué dice el índice alfabético del consulado

Índice oficial: `staatsangehoerigkeit-gesamtnamenverzeichnis-matrikel-chile-data.pdf` (292 páginas, todas
las matrículas conservadas de Chile). Resultado de buscar en el texto completo:

| Apellido | Nombre | Consulado | Band | Nr. |
|---|---|---|---|---|
| VERMEHREN | FRIEDRICH WILHELM AUGUST | SANTIAGO | 1 | 687 |

**Es el único Vermehren de todo Chile.** No aparecen Carlos Oscar Augusto (n. 1873) ni Kurt Roland (n. 1909)
en ningún consulado ni en ningún tomo conservado.

## 2. La inscripción N° 687 (Santiago, Band 1)

Volumen: **PA AA, AB 2/801, "Matrikel 1861–1910"**, imagen 52 (el volumen completo son 65 imágenes).
URL del visor: `https://politisches-archiv.diplo.de/invenio/digitalisat?id=3f406c2c-cbe8-4642-a8c2-db548ba1baca`

Transcripción (manuscrito Kurrent; lo marcado con (?) es lectura dudosa):

| Columna del libro | Contenido |
|---|---|
| N° | 687 |
| Name | Friedrich Wilhelm August Vermehren |
| Stand | Kaufmann (comerciante) |
| Datum der Geburt | 15. Sept. 1845 |
| Geburtsort | Lübeck |
| Kreis / Regierungsbezirk / Religion | — / — / — |
| Datum und Art der Ankunft in Chili | **en blanco** |
| Bemerkung über die Legitimationspapiere | "In Concepción eingetragen, laut Bericht(?) vom Konsulat(?) 14/2.1901" |
| Verheiratet (fecha / con / de) | **en blanco** |
| Kinder | **en blanco** |
| Datum der Eintragung u. Bemerkungen | "Eingetr.: den 5. Januar 1901, auf Grund des **Schutzscheins N° 187** des Kais. Generalkonsulats(?) in **Valparaíso**, und dort in die Matrikel eingetr.; ferner wurde er in die Matrikel eingetr. in **Concepción unter N° 53**." |
| Tinta roja, cruzada | "verstorben — Eintragung: Dezember 1925" + firma |

**Lecturas importantes:**

- **Confirma la identidad:** nacido el 15-09-1845 en Lübeck. Coincide con el acta de bautismo N° 605 que ya
  teníamos y con el perfil alemán de FamilySearch. La fecha "1867" del perfil chileno queda descartada.
- **"1901" no es la llegada a Chile.** Es la fecha en que se inscribió en Santiago (5-ene-1901). La columna
  de llegada está vacía.
- **Hubo dos inscripciones anteriores:** una en Valparaíso (con un *Schutzschein*, certificado de
  protección consular emitido a súbditos del Imperio, N° 187) y otra en Concepción bajo el N° 53. Que el consulado general del
  Imperio le haya emitido un Schutzschein es evidencia de que en ese momento lo trataba como súbdito alemán
  bajo su protección (prueba algo más débil que un Heimatschein, que certifica la nacionalidad).
- **La tinta roja** ("verstorben, Dezember 1925") aparece igual en las entradas 683, 684 y 685 de la misma
  página: es una depuración masiva del libro en 1925, no una fecha de muerte. Es consistente con la muerte en
  Hamburgo el 9-feb-1924.

## 2b. Verificación con OCR automático (2026-09-17)

La transcripción anterior se contrastó con dos modelos gratuitos de reconocimiento de manuscrito, corridos
localmente sobre recortes renglón por renglón: **TrOCR `dh-unibe/trocr-kurrent`** (Kurrent siglo XIX) y
**Kraken 7.1.1 + modelo Zenodo 7933463** (alemán manuscrito general). Los dudosos se revisaron además con
ampliación a nivel de palabra.

| Campo | Lectura humana previa | TrOCR Kurrent | Kraken | Resultado |
|---|---|---|---|---|
| Nombre | Friedrich Wilhelm August Vermehren | "Friedricha Wilhelm / August / Vermehren" | ilegible | ✅ confirmado |
| Stand | Kaufmann | "… / mann" | "Fm / mann" | ✅ confirmado (Kauf- visible en ampliación) |
| Nacimiento | 15. Sept. 1845, Lübeck | "15. Sept. 1845. Jubel" | ilegible | ✅ fecha confirmada; "Lübeck" mal leído por el modelo, claro en la imagen |
| Obs. línea 1 | Eingetr.: den 5. Januar 1901, auf Grund | "…den 5t. Jenner 1901. auf Grund" | parcial | ✅ confirmado ("Jenner" = forma antigua de Januar) |
| Obs. línea 2 | des **Heimatscheins** N 187 des Kais. Konsulats | "des **Schutzscheines** Nr. 887 des Kais: …" | "Des Sratzecheieres **A 187** das Siſ: …" | ⚠️ **CORREGIDO a Schutzscheins** (ambos modelos + ampliación); **N° 187** confirmado por Kraken y ampliación (TrOCR leyó 887); última palabra probable "Generalkonsulats" (sin confirmar) |
| Obs. línea 3 | in Valparaíso, und dort in die Matrikel | "in Valpereise, verdort in die materibus" | parcial | ✅ confirmado |
| Obs. línea 5 | in Concepción unter N° 53 | "in Conzeptien unter Nr. 53." | ilegible | ✅ confirmado |
| Legitimation l.1–2 | In Concepción eingetragen | "In machen / eingetragen" | "… / ingetrert" | ✅ "eingetragen" confirmado; "Concepcion" claro en ampliación |
| Legitimation l.3–4 | (ilegible) | "Soñtbaricht / venkursälag" | "vin klrrück / enichla" | ⚠️ lectura probable "laut Bericht vom Konsulat" — no confirmada |
| Legitimation l.5 | 14/2.1901 | "14/2.1901" | ilegible | ✅ confirmado |

Índice de Hamburgo 1924 (misma prueba): apellido **Vermehren** confirmado exacto por TrOCR; "Wilh. Aug."
confirmado; Standesamt **22** confirmado. Los números **492** y **9/2** no los leyó bien ningún modelo (fallan
con cifras sueltas), pero la lectura humana es nítida y cuadra con el Findbuch (N° 492 cae en el tomo
0001–0496, fechas 01.01–10.07.1924).

**Conclusión:** la transcripción se sostiene, con una corrección de fondo: el documento de Valparaíso era un
**Schutzschein** (certificado de protección consular), no un Heimatschein.

## 3. Se buscaron las inscripciones anteriores — están en tomos perdidos

| Registro citado | Qué se encontró en el PA AA |
|---|---|
| Valparaíso (Schutzschein N° 187) | Las matrículas de Valparaíso conservadas empiezan en **1906** (AB 2/923 en adelante). Todo lo anterior no existe en el archivo. |
| Concepción N° 53 | Hay dos tomos: **AB 2/171** (1892–1909, "Band I") y **AB 2/172** (1877–1938, "Band II"). La portada del Band I lleva la nota **"Vorgängerband nicht mehr vorhanden"** (el tomo anterior ya no existe) y su numeración empieza en N° 139. En el Band II, la N° 53 es **Friedrich Max Frick (1902)**, no Vermehren. La N° 53 que cita Santiago estaba en el tomo perdido. |

**Consecuencia:** las fechas de las inscripciones de Valparaíso y Concepción no se pueden recuperar del
archivo. La inscripción de Santiago es la única que sobrevive, y solo prueba de forma indirecta que existieron.

## 4. La regla de los 10 años (§ 21 de la ley de 1870)

Texto legal verificado (Gesetz über die Erwerbung und den Verlust der Bundes- und Staatsangehörigkeit,
1-jun-1870, vigente desde el 1-ene-1871 hasta la ley de 1913, que la derogó desde el 1-ene-1914):

> § 21 Abs. 1: "Norddeutsche, welche das Bundesgebiet verlassen und sich zehn Jahre lang ununterbrochen im
> Auslande aufhalten, verlieren dadurch ihre Staatsangehörigkeit."
>
> § 21 Abs. 2: "Der hiernach eingetretene Verlust der Staatsangehörigkeit erstreckt sich zugleich auf die
> Ehefrau und die unter väterlicher Gewalt stehenden minderjährigen Kinder, soweit sie sich bei dem
> Ehemanne, beziehungsweise Vater befinden."

El plazo se **interrumpía** con la inscripción en la matrícula de un consulado, y volvía a correr desde el
día siguiente a la baja de la matrícula. También corría desde el vencimiento del pasaporte o Heimatschein si
la persona tenía uno. Un regreso a Alemania también cortaba la estadía "ininterrumpida".

Jurisprudencia aplicable — **BVerwG, sentencia 1 C 28.20 del 30-mar-2021** (caso de emigrantes a Brasil,
estructura muy parecida):

- El § 21 **también se aplica a los hijos nacidos en el extranjero** que nunca vivieron en Alemania (Rn. 20).
- Para ellos, el plazo de 10 años **empieza a correr al cumplir la mayoría de edad** (Rn. 19–20).
- Mientras eran menores, perdían la nacionalidad solo si la perdía el padre y vivían con él (Abs. 2).

## 5. Búsqueda de Carlos Oscar Augusto y Kurt Roland en los registros consulares (2026-09-17)

| Fuente revisada | Método | Resultado |
|---|---|---|
| Índice alfabético de todas las matrículas conservadas de Chile (consulado de Santiago, 7.641 registros) | Búsqueda de texto + búsqueda difusa de variantes del apellido (Vermehren, Vermeren, Wermehren, Fermehren, Vermehr, etc.) + búsqueda por nombres de pila (Carlos/Karl + Oscar/Oskar; Roland) con cualquier apellido | Solo aparece Friedrich Wilhelm August (Santiago 1/687). No se ubicaron registros de Carlos Oscar ni de Kurt Roland. |
| Santiago, Matrikel 1861–1910 (AB 2/801) | Revisión visual de la sección de la letra V (N° 681–687) y secciones vecinas U y W | Solo Friedrich Wilhelm August (N° 687). |
| Valparaíso, Namenverzeichnis 1906–1938 (AB 2/926) | Revisión visual de la página de la letra V | No se ubicaron registros Vermehren. |
| Valparaíso, índice de Passregister 1907–1920 y 1922–1924 (AB 2/933) | Revisión visual de las páginas de la letra V | No se ubicaron registros Vermehren. |
| Santiago, Matrikel 1911–1927 y 1928–1943 (AB 2/802, 803) | Cubiertos por el índice alfabético del consulado | No se ubicaron registros Vermehren. |

**Lo que NO se pudo revisar** (y por qué la búsqueda no es concluyente):

- **Valparaíso antes de 1906:** los libros no se conservan en el Politisches Archiv.
- **Concepción antes de ~1892:** el tomo anterior figura como "nicht mehr vorhanden".
- **Pasaportes, Schutzscheine o Heimatscheine** emitidos en esos años: si existieron, estarían en esos
  libros perdidos o en manos de la familia.
- **Santiago, Passregister 1914–1943** (AB 2/813–815): no revisados (posteriores a 1909).
- Registros en consulados fuera de Chile o en autoridades en Alemania (si hubo viajes o estadías allá).

## 6. Qué significa para el caso — punto a evaluar con el abogado

La vía § 5 StAG requiere que Amelia (n. 1939) tuviera la nacionalidad alemana al nacer Eileen, lo que
depende de la continuidad de la nacionalidad en cada generación anterior.

Según el § 21 de la ley de 1870 y el fallo BVerwG 1 C 28.20, para las personas nacidas en el extranjero
antes de 1914 es relevante si existe documentación consular (matrícula, pasaporte, Schutzschein o
Heimatschein) o de estadías en Alemania en los años posteriores a su mayoría de edad.

- **Friedrich Wilhelm August:** hay al menos tres inscripciones consulares (Valparaíso, Concepción,
  Santiago 1901) y un Schutzschein.
- **Carlos Oscar Augusto (n. 1873):** en los registros conservados revisados **no se ubicó documentación
  consular a su nombre**. Como faltan libros de Valparaíso y Concepción, eso no permite concluir nada por sí
  solo. **Es el punto que conviene evaluar con un abogado especialista antes de avanzar**, y el tipo de
  documento que más ayudaría a reunir.

**Documentos que sería valioso ubicar en la familia** (período aproximado 1890–1914): pasaportes o
documentos alemanes de Carlos Oscar, certificados emitidos por consulados alemanes, libretas militares,
cartas o pasajes que muestren viajes o estadías en Alemania.

## 7. Cómo comunicarse con autoridades y archivos

Ver `contactos-y-solicitudes.md`. Criterio: enviar lo que el consulado pide (la inscripción de la matrícula),
pedir solo búsquedas y copias, hacer preguntas abiertas y **no pedir a ninguna autoridad que evalúe por
escrito si alguien perdió la nacionalidad** — esa evaluación la hace el abogado.

---

## 8. ¿Los viajes a Alemania interrumpen el plazo de 10 años? (2026-09-17)

**Regla.** El § 21 BuStAG 1870 exige diez años **ininterrumpidos** de residencia en el extranjero
("zehn Jahre lang ununterbrochen im Auslande"). En consecuencia:

- **La estadía en territorio alemán interrumpe el plazo**, y al salir de nuevo empieza a correr un
  plazo nuevo de diez años.
- También lo interrumpen o impiden la **inscripción en la matrícula consular** y la emisión o
  renovación de un pasaporte / Heimatschein / Schutzschein (el plazo corre desde el vencimiento del papel).
- **La regla se derogó con la RuStAG 1913, vigente desde el 01-01-1914.** Solo importan los plazos
  de diez años que se hayan **completado antes de esa fecha**.

**Cómo juega con lo que tenemos** (a confirmar con abogado; no es asesoría legal):

| Persona | Indicio | Efecto que habría que evaluar |
|---|---|---|
| Friedrich Wilhelm August (n. 1845) | Embarca en Hamburgo en 1886 y en 1909; matrícula de Santiago N° 687 con Schutzschein N° 187 | Cada estadía en Alemania reiniciaría el plazo. Desde 1909 a 1914 hay 5 años: no alcanzaría a completarse |
| Carlos Oscar Augusto (n. 1873) | Posible embarque en Hamburgo en 1891 a los 17 (por confirmar) | Siendo menor, en 1891 su situación seguía a la del padre. Según BVerwG 1 C 28.20 su propio plazo correría desde la mayoría de edad (21 años, ~1894) |

**La ventana decisiva para Carlos Oscar es 1894–1904.** Cualquier prueba de que estuvo en Alemania,
o de que tuvo papeles alemanes vigentes (pasaporte, Heimatschein, inscripción consular) en esos
años, cerraría el punto: el plazo se reiniciaría y ya no podría completarse antes del 01-01-1914.

**Búsquedas hechas (2026-09-17).** Todas las fuentes en línea y gratuitas que indexan nombres:

| Fuente | Alcance | Resultado para nuestra familia |
|---|---|---|
| ACTApro — listas de pasajeros de Hamburgo, "Vermehren" 1890–1915 | 18 fichas | Ningún Vermehren de la edad de Carlos Oscar con rumbo a Chile en 1894–1904 (las de esos años son otras familias: Sardinia 1899 a México, Kurfürst 1902 "Hans, 21" a Sudáfrica, König Wilhelm II 1908 "Wilhelm, 23", Cap Vilano 1910 "Elisabeth, 18") |
| ACTApro — todo el archivo, "Vermehren" 1850–1945 | 172 registros | Ninguno a nombre de Friedrich Wilhelm August ni de Carlos Oscar Augusto (los expedientes personales son de otras ramas Vermehren de Hamburgo) |
| Staatsarchiv Hamburg, 332-8 Meldewesen — **Reisepassprotokolle, registro alfabético 1855–1897** (PDF libre) | Pasaportes emitidos por la policía de Hamburgo | Bajo "Vermehren" figuran Bernhard, Carl Emil Johann (1868) y Hermann Wilhelm Moritz (Güstrow). Ninguno de los nuestros. Imagen en `02-.../indices-hamburgo-revisados/` |
| Staatsarchiv Hamburg, 332-8 — **Fremdenmeldeprotokolle (hombres), registro alfabético 1868–1889** (PDF libre) | Inscripción policial en Hamburgo | 13 entradas Vermehren, ninguna corresponde (los de Lübeck son Paul, Paul Ad. y Rich., otras personas). Imagen en la misma carpeta |
| **Consulado de Valdivia — Namenverzeichnis de la Matrikel (PA AA AB 2/916, 1872–1938)** | Índice alfabético completo del tomo AB 2/915 | Bajo la letra V: Vogg, Voss, Vidal, Valta, Vogt, Vervier, Vonnoh, Vosberg, Vogel, Vierig, Voge, Vogelskamp, Vorreiter, Volk, Voelker. **Ningún Vermehren** |
| **Consulado de Valdivia — Passregister (PA AA AB 2/918, 1880–1930)** | Páginas 8 a 17 del libro, entradas 52 a 195 = **1892 a 1908** (cubre entera la ventana 1894–1904) | **Ningún Vermehren.** Faltan por revisar las entradas 1880–1892 y las posteriores a 1908 |
| Archivo de la Hansestadt Lübeck — buscador en línea, "Vermehren" | 121 registros | Expedientes de otras ramas (senadores, comerciantes). El buscador **no indexa padrones ni fichas de habitantes**, así que esto no descarta nada |
| Staatsarchiv Bremen — listas de pasajeros | — | Las listas de **1875 a 1908 fueron destruidas** por falta de espacio; solo sobreviven restos de 1907/08 y 1913/14. Esa vía no existe |

Valdivia se revisó el 17-09-2026 porque el aviso fúnebre de 1926 sitúa allí a un hijo,
"August Vermehren und Frau geb. Heffner (Valdivia, Chile)". A diferencia de Valparaíso y
Concepción, el tomo de Valdivia **sí se conserva desde 1872** y arranca con su primera
inscripción, sin tomo predecesor perdido. Imágenes en el expediente Scheihing,
`evidencia/matricula-valdivia-PAAA/` (mismo archivo de origen, PA AA invenio).

**Limitaciones importantes:**
- Las listas de Hamburgo son de **salidas** de emigrantes por ese puerto: no registran entradas a
  Alemania ni viajes por Bremen, Amberes, Liverpool u otros puertos.
- Los pasajeros que no viajaban como emigrantes podían no quedar en estas listas.
- El registro de forasteros de Hamburgo solo cubre 1868–1889 y solo a quienes tenían obligación de
  inscribirse; el padrón general de habitantes empieza en 1892 y **no está digitalizado**.
- Son índices transcritos, con erratas posibles en nombres y edades.

**Lo que queda, y ya no se puede hacer en línea** (hay que escribir o ir):

1. **Archivo de la Hansestadt Lübeck** — series que existen y cubren la ventana, pero no están
   indexadas por nombre en línea:
   - Padrón de habitantes: el Einwohnermeldeamt de Lübeck se crea en 1883–1884
     (expediente `01.1-01 (5) : 24392`); los registros de inscripción están en
     `02.06 Staatliche Polizeiverwaltung Lübeck`.
   - `Heimatberechtigung (= Heimatscheine), Staatsangehörigkeit pp.` — serie de expedientes de
     emisión de Heimatscheine, con tomos hasta 1884, y `Ausstellung von Heimatscheinen und
     ähnlichen Ausweispapieren (Reichs- und Staatsangehörigkeitsgesetz)` para el período posterior.
   - `Passangelegenheiten` (pasaportes) y `Liste der ausgestellten Heimatscheine`.
2. **Staatsarchiv Hamburg** — padrón de habitantes desde 1892 (332-8 Meldewesen), no digitalizado:
   sirve además para confirmar el domicilio de Sievekingsallee 10 en 1922–1924.
3. **Politisches Archiv (Berlín)** — registros de pasaportes y Schutzscheine de los consulados
   alemanes en Chile (pregunta ya incluida en el borrador §3 de `contactos-y-solicitudes.md`).
4. **Papeles de familia** — pasaportes, visas, libretas, cartas o fotos fechadas en Alemania.
5. **Ancestry** (suscripción) — imágenes de las listas de pasajeros, para confirmar identidades.
6. **Consulado de Osorno (PA AA AB 2/596, 1883–1925)** — sin revisar. Y en Valdivia faltan los
   tramos del Passregister anteriores a 1892 y posteriores a 1908.
