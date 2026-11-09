const allowedTags = new Set(['P', 'BR', 'STRONG', 'B', 'EM', 'I', 'U', 'UL', 'OL', 'LI', 'DIV', 'SPAN'])
const blockedTags = new Set(['SCRIPT', 'STYLE', 'IFRAME', 'OBJECT', 'EMBED', 'SVG', 'MATH', 'FORM', 'TEMPLATE'])

export function sanitizeRichText(input: string): string {
  const parsed = new DOMParser().parseFromString(input, 'text/html')
  const output = document.createElement('div')

  function appendSafe(node: Node, parent: Node) {
    if (node.nodeType === Node.TEXT_NODE) {
      parent.appendChild(document.createTextNode(node.textContent || ''))
      return
    }
    if (node.nodeType !== Node.ELEMENT_NODE) return

    const element = node as Element
    if (blockedTags.has(element.tagName)) return

    // Only known formatting tags are copied. Attributes and links are discarded.
    const safeElement = allowedTags.has(element.tagName)
      ? document.createElement(element.tagName.toLowerCase())
      : parent
    if (safeElement !== parent) parent.appendChild(safeElement)
    element.childNodes.forEach((child) => appendSafe(child, safeElement))
  }

  parsed.body.childNodes.forEach((node) => appendSafe(node, output))
  return output.innerHTML
}

export function richTextToPlainText(input: string): string {
  const container = document.createElement('div')
  container.innerHTML = sanitizeRichText(input)

  function readText(node: Node): string {
    if (node.nodeType === Node.TEXT_NODE) return node.textContent || ''
    if (node.nodeType !== Node.ELEMENT_NODE) return ''
    const element = node as Element
    const text = Array.from(element.childNodes).map(readText).join('')
    return ['P', 'DIV', 'LI', 'BR'].includes(element.tagName) ? text + ' ' : text
  }

  return Array.from(container.childNodes).map(readText).join('').replace(/\s+/g, ' ').trim()
}
