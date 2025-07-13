import { Pipe, PipeTransform } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { Observable, of } from 'rxjs';
import { map, catchError, shareReplay } from 'rxjs/operators';

@Pipe({
  name: 'svg',
  standalone: true,
  pure: false // Importante para que funcione con observables
})
export class SvgPipe implements PipeTransform {
  private cachedSvgs = new Map<string, Observable<SafeHtml>>();

  constructor(
    private http: HttpClient,
    private sanitizer: DomSanitizer
  ) { }

  transform(url: string, color?: string): Observable<SafeHtml> {
    const cacheKey = `${url}:${color || 'default'}`;

    if (!this.cachedSvgs.has(cacheKey)) {
      const svg$ = this.http.get(url, { responseType: 'text' })
        .pipe(
          map(svg => {
            let modifiedSvg = svg;

            // Si se especifica un color, reemplazar el valor de fill
            if (color) {
              modifiedSvg = svg.replace('fill="currentColor"', `fill="${color}"`);
            }

            return this.sanitizer.bypassSecurityTrustHtml(modifiedSvg);
          }),
          catchError(error => {
            console.error(`Error loading SVG from ${url}:`, error);
            return of(this.sanitizer.bypassSecurityTrustHtml(''));
          }),
          shareReplay(1) // Compartir el resultado entre múltiples suscriptores
        );

      this.cachedSvgs.set(cacheKey, svg$);
    }

    return this.cachedSvgs.get(cacheKey)!;
  }
}
