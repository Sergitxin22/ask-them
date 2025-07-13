import { Component, Input, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { DomSanitizer, SafeHtml } from '@angular/platform-browser';
import { AsyncPipe, CommonModule } from '@angular/common';
import { SvgPipe } from '../../../../pipes/svg/svg.pipe';
import { Usuario } from '../../../../models/models';

@Component({
  selector: 'app-header',
  imports: [CommonModule, AsyncPipe, SvgPipe],
  templateUrl: './header.component.html',
  styleUrl: './header.component.css',
  standalone: true
})
export class HeaderComponent implements OnInit {
  svgContent: SafeHtml | null = null;
  @Input() user: Usuario | null = null;

  constructor(private http: HttpClient, private sanitizer: DomSanitizer) { }

  ngOnInit() {
    this.loadSvg();
  }

  loadSvg() {
    this.http.get('assets/images/coins.svg', { responseType: 'text' })
      .subscribe({
        next: (svg) => {
          // No reemplazamos el fill, mantenemos currentColor
          this.svgContent = this.sanitizer.bypassSecurityTrustHtml(svg);
        },
        error: (error) => {
          console.error('Error loading SVG:', error);
        }
      });
  }
}
